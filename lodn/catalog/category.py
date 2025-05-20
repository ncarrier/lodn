from enum import Enum


class Category(Enum):
    FAUNA = "faune"
    FLORA = "flore"
    NON_FIGURATIVE = "non figuratif"
    OBJECT = "objet"
    POUCH = "pochette"


if __name__ == "__main__":
    print(Category.POUCH.value)
    for c in Category:
        print(c.value.capitalize())
    print(list(Category))
    print(Category.OBJECT.value)
