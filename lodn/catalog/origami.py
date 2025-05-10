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
    def categorie(self):
        return self.__meta.get("categorie", None)

    @property
    def commentaires(self):
        return self.__meta.get("commentaires", None)

    @property
    def diametre(self):
        return self.__meta.get("diametre", None)

    @property
    def hauteur(self):
        return self.__meta.get("hauteur", None)

    @property
    def largeur(self):
        return self.__meta.get("largeur", None)

    @property
    def longueur(self):
        return self.__meta.get("longueur", None)

    @property
    def quotation(self):
        return self.__meta.get("quotation", None)

    @property
    def types(self):
        return self.__meta.get("types", None)
    # end of properties from the meta.jon file

    def __str__(self):
        return (f"{self.name=} - {self.types=} - {self.quotation=} - "
                f"{self.commentaires=} - {self.longueur=} - {self.hauteur=} - "
                f"{self.largeur=} - {self.diametre=}")
