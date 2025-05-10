from os import listdir
from lodn.catalog.origami import Origami


class Catalog(object):
    def __init__(self, path):
        self.__catalog = []
        for f in listdir(path):
            self.__catalog.append(Origami(f"{path}/{f}"))
