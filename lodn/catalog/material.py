from enum import Enum


class Material(Enum):
    FABRIC_NAPKIN = "serviette en tissu"
    PAPER_NAPKIN = "serviette en papier"
    KAMI = "papier kami"
    BRISTOL = "bristol"
    KRAFT = "kraft"
    SILK_PAPER = "paper de soie"
    SPONGE_NAPKIN = "serviette en éponge"


if __name__ == "__main__":
    for m in Material:
        print(m.value.capitalize(), m.name)
    n = Material("bristol")
    print(n.name)
    print(Material._member_map_.values())
    print([m.value for m in Material])
