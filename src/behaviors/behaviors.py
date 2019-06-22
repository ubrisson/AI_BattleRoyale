from enum import Enum, auto
from random import randint


class Behavior(Enum):
    RANDFULL = auto()
    RANDKILL = auto()
    IDLE = auto()
    DETASC = auto()
    DETDESC = auto()
    KILLBEST = auto()
    DEFAULT = auto()


def rand_behavior() -> Behavior:
    r = randint(1, Behavior.DEFAULT.value) - 1
    return list(Behavior)[r]
