import random
from enum import Enum, auto


class Behavior(Enum):
    RANDFULL = auto()
    RANDKILL = auto()
    IDLE = auto()
    DETASC = auto()
    DETDESC = auto()
    KILLBEST = auto()


def rand_behavior() -> Behavior:
    return random.choice(list(Behavior))
