from enum import Enum


class Material(Enum):
    FABRIC_NAPKIN = "serviette en tissu"
    PAPER_NAPKIN = "serviette en papier"
    KAMI = "papier kami"
    BRISTOL = "bristol"
    # KRAFT = "kraft"
    # SILK_PAPER = "silk paper"
    # SPONGE_NAPKIN = "sponge napkin"


if __name__ == "__main__":
    for m in Material:
        print(m.value.capitalize(), m.name)
    n = Material("bristol")
    print(n.name)
