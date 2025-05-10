import json
import os


class Origami:
    def __init__(self, path):
        self.__path = path
        with open(f"{path}/meta.json") as f:
            self.__meta = json.load(f)

    @property
    def name(self):
        return os.path.basename(self.__path)

    # properties from the meta.jon file
    @property
    def category(self):
        return self.__meta.get("category", None)

    @property
    def comment(self):
        return self.__meta.get("comment", None)

    @property
    def diameter(self):
        return self.__meta.get("diameter", None)

    @property
    def height(self):
        return self.__meta.get("height", None)

    @property
    def length(self):
        return self.__meta.get("length", None)

    @property
    def materials(self):
        return self.__meta.get("materials", None)

    @property
    def quotation(self):
        return self.__meta.get("quotation", None)

    @property
    def width(self):
        return self.__meta.get("width", None)
    # end of properties from the meta.jon file

    def __str__(self):
        return (f"{self.name=} - {self.category=} - {self.comment=} - "
                f"{self.diameter=} - {self.height=} - {self.length=} - "
                f"{self.materials=} - {self.quotation=} - {self.width}")
