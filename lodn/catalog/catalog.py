from os import listdir
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

    def export(self, path):
        env = Environment(
            loader=FileSystemLoader('templates'),
            autoescape=select_autoescape()
        )
        template = env.get_template("template.tpl")

        # organize the catalog by sections
        catalog = {c.value: [] for c in Category}
        for o in self.catalog:
            for c in Category:
                if c.value == o.category:
                    catalog[c.value].append(o)

        # prepare the list of materials, for filtering
        materials = [m.value for m in Material]
        # dump the html
        html = template.render(
            catalog=catalog,
            materials=materials
        )
        with open(f"{path}/index.html", "w") as f:
            f.write(html)

        # TODO copy style.css, images...
