from abc import ABC, abstractmethod
from typing import List

from src.behaviors import deterministic_behaviors as det
from src.behaviors import random_behaviors as rd
from src.behaviors.behaviors import Behavior


class Player(ABC):
    def __init__(self, id_player: int):
        self.id: int = id_player
        self.kills: int = 0
        self.alive: bool = True
        self.killed: bool = False
        self.behavior: Behavior = Behavior.DEFAULT

    @abstractmethod
    def play(self, players: List["Player"]):
        pass

    def die(self):
        self.alive = not self.killed

    def __repr__(self):
        return f" {self.id} : {self.kills}"


def new_player(behavior: Behavior, id_player: int) -> Player:
    if behavior == Behavior.RANDFULL:
        return RandFullPlayer(id_player)
    elif behavior == Behavior.RANDKILL:
        return RandKillPlayer(id_player)
    elif behavior == Behavior.IDLE:
        return IdlePlayer(id_player)
    elif behavior == Behavior.DETASC:
        return DetAscPlayer(id_player)
    elif behavior == Behavior.DETDESC:
        return DetDescPlayer(id_player)
    elif behavior == Behavior.KILLBEST:
        return KillBestPlayer(id_player)
    elif behavior == Behavior.DEFAULT:
        return IdlePlayer(id_player)


class RandKillPlayer(Player):
    def __init__(self, id_player: int):
        super().__init__(id_player)
        self.behavior = Behavior.RANDKILL

    def play(self, players: List[Player]):
        rd.rand_kill(self, players)


class RandFullPlayer(Player):
    def __init__(self, id_player: int):
        super().__init__(id_player)
        self.behavior = Behavior.RANDFULL

    def play(self, players: List[Player]):
        rd.rand_act(self, players)


class IdlePlayer(Player):
    def __init__(self, id_player: int):
        super().__init__(id_player)
        self.behavior = Behavior.IDLE

    def play(self, players: List[Player]):  # do nothing
        a = 1


class DetAscPlayer(Player):

    def __init__(self, id_player: int):
        super().__init__(id_player)
        self.behavior = Behavior.DETASC

    def play(self, players: List[Player]):
        det.kill_asc(self, players)


class DetDescPlayer(Player):

    def __init__(self, id_player: int):
        super().__init__(id_player)
        self.behavior = Behavior.DETDESC

    def play(self, players: List[Player]):
        det.kill_desc(self, players)


class KillBestPlayer(Player):

    def __init__(self, id_player: int):
        super().__init__(id_player)
        self.behavior = Behavior.KILLBEST

    def play(self, players: List[Player]):
        det.kill_best(self, players)
