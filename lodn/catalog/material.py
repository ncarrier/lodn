from enum import Enum


class Material(Enum):
    FABRIC_NAPKIN = "fabric napkin"
    PAPER_NAPKIN = "paper napkin"
    KAMI = "kami"
    BRISTOL = "bristol"
    KRAFT = "kraft"
    SILK_PAPER = "silk paper"
    SPONGE_NAPKIN = "sponge napkin"


if __name__ == "__main__":
    print(Material.KAMI.value)
    i = 0
    for m in Material:
        print(m.value.capitalize(), i)
        i += 1
