from os import listdir
import shutil
from lodn.catalog.origami import Origami
from lodn.catalog.category import Category
from lodn.catalog.material import Material
from jinja2 import Environment, FileSystemLoader, select_autoescape


class Catalog(object):
    def __init__(self, path):
        self.__catalog = []
        for f in sorted(listdir(path)):
            o = Origami(f"{path}/{f}")
            self.__catalog.append(o)

    @property
    def catalog(self):
        return self.__catalog

    def get_by_name(self, name):
        for o in self.catalog:
            if o.name == name:
                return o

        return None

    def __organize_catalog_by_sections(self):
        catalog = {c.value: [] for c in Category}
        for o in self.catalog:
            for c in Category:
                if c.value == o.category:
                    catalog[c.value].append(o)

        return catalog

    def __get_materials_list(self):
        return [m.value for m in Material]

    @staticmethod
    def __dump_html(path, catalog, materials):
        env = Environment(
            loader=FileSystemLoader('templates'),
            autoescape=select_autoescape()
        )
        template = env.get_template("template.tpl")

        html = template.render(
            catalog=catalog,
            materials=materials
        )
        with open(f"{path}/index.html", "w") as f:
            f.write(html)

    def __copy_resources(self, path):
        for o in self.catalog:
            try:
                shutil.copyfile(o.photo_path, f"{path}/{o.name}.png")
            except FileNotFoundError:
                shutil.copyfile(
                    Origami.PLACEHOLDER_PHOTO,
                    f"{path}/{o.name}.png"
                )

        for r in ["style.css", "lodn.js", "favicon.svg"]:
            src = f"{Origami.RESOURCES}/{r}"
            dst = f"{path}/{r}"
            shutil.copyfile(src, dst)

    def export(self, path):
        catalog = self.__organize_catalog_by_sections()
        materials = self.__get_materials_list()

        Catalog.__dump_html(path, catalog, materials)
        self.__copy_resources(path)
