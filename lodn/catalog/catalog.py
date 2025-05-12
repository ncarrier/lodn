from os import listdir
from lodn.catalog.origami import Origami


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
