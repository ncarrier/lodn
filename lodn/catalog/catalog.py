from os import listdir
from lodn.catalog.origami import Origami
from lodn.catalog.category import Category
from jinja2 import Environment, FileSystemLoader, select_autoescape


class Catalog(object):
    def __init__(self, path):
        self.__catalog = []
        for f in listdir(path):
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
        print("exporting")  # TODO
        env = Environment(
            loader=FileSystemLoader('templates'),
            autoescape=select_autoescape()
        )
        template = env.get_template("template.tpl")
        data = {c.value: [] for c in Category}
        for o in self.catalog:
            for c in Category:
                if c.value == o.category:
                    data[c.value].append(o)
        html = template.render(data=data)
        with open(f"{path}/index.html", "w") as f:
            f.write(html)

        # TODO copy style.css, images...
