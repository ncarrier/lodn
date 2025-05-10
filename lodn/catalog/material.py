from enum import Enum


class Material(Enum):
    BRISTOL = "bristol"
    FABRIC_NAPKIN = "fabric napkin"
    KAMI = "kami"
    KRAFT = "kraft"
    PAPER_NAPKIN = "paper napkin"
    SILK = "silk"
    SPONGE_NAPKIN = "sponge napkin"


if __name__ == "__main__":
    print(Material.KAMI.value)
    for m in Material:
        print(m.value.capitalize())
