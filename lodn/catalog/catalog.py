from os import listdir, symlink, replace
import shutil
from glob import glob
from os.path import basename
from jinja2 import Environment, FileSystemLoader, select_autoescape

from lodn.catalog.origami import Origami
from lodn.catalog.category import Category
from lodn.catalog.material import Material


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

    @staticmethod
    def __dump_html(path, catalog):
        env = Environment(
            loader=FileSystemLoader('templates'),
            autoescape=select_autoescape()
        )
        template = env.get_template("template.tpl")
        html = template.render(
            catalog=catalog,
            materials=Material,
            hourly_rate=70,  # TODO where to put this parameter ?
        )
        with open(f"{path}/catalog.html", "w") as f:
            f.write(html)

    def __copy_resources(self, path):
        for o in self.catalog:
            o.pil_image.save(f"{path}/{o.name}.jpg", "JPEG")

        for src in glob(f"{Origami.RESOURCES}/*"):
            dst = f"{path}/{basename(src)}"
            shutil.copyfile(src, dst)

        symlink("catalog.html", f"{path}/index.html~")
        replace(f"{path}/index.html~", f"{path}/index.html")

    def export(self, path):
        catalog = self.__organize_catalog_by_sections()
        Catalog.__dump_html(path, catalog)
        self.__copy_resources(path)

    def __str__(self):
        res = ""
        for o in self.__catalog:
            res += f"{str(o)}\n"

        return res
