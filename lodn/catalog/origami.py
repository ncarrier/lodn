import json
import os


class Origami:
    def __init__(self, path):
        self.__path = path
        self.__json_path = f"{path}/meta.json"
        with open(self.__json_path) as f:
            try:
                self.__meta = json.load(f)
            except json.decoder.JSONDecodeError:
                self.__meta = json.loads("{}")

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
        v = variables
        json_dict = {
            "category": v.category.get(),
            "comment": v.comment.get(),
            "diameter": v.diameter.get(),
            "paper_size": v.paper_size.get(),
            "height": v.height.get(),
            "length": v.length.get(),
            "width": v.width.get(),
            "materials": v.materials,
            "quotation": v.quotation.get()
        }
        # TODO if name has changed, move the folder
        dump = json.dumps(json_dict, indent=4)
        with open(self.__json_path, "w") as f:
            f.write(dump)
        self.__meta = json.loads(dump)
