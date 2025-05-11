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
        return self.__meta.get("category", "object")

    @property
    def comment(self):
        return self.__meta.get("comment", "")

    @property
    def diameter(self):
        return self.__meta.get("diameter", 0)

    @property
    def height(self):
        return self.__meta.get("height", 0)

    @property
    def length(self):
        return self.__meta.get("length", 0)

    @property
    def materials(self):
        return self.__meta.get("materials", [])

    @property
    def paper_size(self):
        return self.__meta.get("paper_size", 0)

    @property
    def quotation(self):
        return self.__meta.get("quotation", 0)

    @property
    def width(self):
        return self.__meta.get("width", 0)
    # end of properties from the meta.jon file

    def __str__(self):
        return (f"{self.name=} - {self.category=} - {self.comment=} - "
                f"{self.diameter=} - {self.height=} - {self.length=} - "
                f"{self.materials=} - {self.quotation=} - {self.width}")

    def save(self, variables):
        # v = variables
        # print(f"{v.name.get()=}, {v.category.get()=}, {v.comment.get()=}"
        #       f", {v.paper_size.get()=}, {v.diameter.get()=}"
        #       f", {v.height.get()=}, {v.length.get()=}"
        #       f", {v.width.get()=}, {v.materials=}"
        #       f", {v.quotation.get()=}")
        pass
