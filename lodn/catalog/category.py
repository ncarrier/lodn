from enum import Enum


class Category(Enum):
    FAUNA = "fauna"
    FLORA = "flora"
    NON_FIGURATIVE = "non figurative"
    OBJECT = "object"
    POUCH = "pouch"


if __name__ == "__main__":
    print(Category.POUCH.value)
    for c in Category:
        print(c.value.capitalize())
    print(list(Category))
