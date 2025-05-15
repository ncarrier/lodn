import json
import os
import shutil
from glob import glob
from PIL import Image, ImageTk


class Origami:
    IMG_WIDTH = 400
    IMG_HEIGHT = 400
    RESOURCES = f"{os.path.dirname(__file__)}/../../resources"
    PLACEHOLDER_PHOTO = f"{RESOURCES}/no_photo.jpg"

    def __init__(self, path):
        self.__setup_paths(path)
        self.__meta = json.loads("{}")
        try:
            with open(self.__json_path) as f:
                try:
                    self.__meta = json.load(f)
                except json.decoder.JSONDecodeError:
                    pass
        except FileNotFoundError:
            pass
        self.__load_photo()

    def __setup_paths(self, path):
        self.__path = path
        self.__json_path = f"{path}/meta.json"
        self.__photo_path = f"{path}/photo.jpg"
        self.__instructions_glob = f"{path}/instructions.*"

    def __load_photo(self):
        try:
            image = Image.open(self.__photo_path)
        except FileNotFoundError:
            image = Image.open(Origami.PLACEHOLDER_PHOTO)

        image.thumbnail((Origami.IMG_WIDTH, Origami.IMG_HEIGHT))
        self.__photo = ImageTk.PhotoImage(image)

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

    @property
    def photo(self):
        return self.__photo

    @property
    def photo_path(self):
        return self.__photo_path

    @property
    def has_instructions(self):
        return len(glob(self.__instructions_glob)) != 0

    @property
    def instructions(self):
        if not self.has_instructions:
            return None

        return glob(self.__instructions_glob)[0]

    @photo.setter
    def photo(self, path):
        shutil.copyfile(path, self.__photo_path)
        self.__load_photo()

    def __str__(self):
        return (f"{self.name=} - {self.category=} - {self.comment=} - "
                f"{self.diameter=} - {self.height=} - {self.length=} - "
                f"{self.materials=} - {self.quotation=} - {self.width}")

    def save(self, variables):
        v = variables
        new_name = v.name.get()
        if new_name != self.name:
            src = self.__path
            dst = f"{os.path.dirname(self.__path)}/{new_name}"
            shutil.move(src, dst)
            self.__setup_paths(dst)
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
        dump = json.dumps(json_dict, indent=4)
        with open(self.__json_path, "w") as f:
            f.write(dump)
        self.__meta = json.loads(dump)
