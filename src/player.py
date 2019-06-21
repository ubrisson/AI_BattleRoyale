from abc import ABC, abstractmethod
from typing import List

from src.behaviors import deterministic_behaviors as det
from src.behaviors import random_behaviors as rd


class Player(ABC):
    def __init__(self, id_player: int):
        self.id: int = id_player
        self.kills: int = 0
        self.alive: bool = True
        self.killed: bool = False
        self.behavior = "default"

    @abstractmethod
    def play(self, players: List["Player"]):
        pass

    def die(self):
        self.alive = not self.killed

    def __repr__(self):
        return f" {self.id} : {self.kills}"


class RandKillPlayer(Player):
    def __init__(self, id_player: int):
        super().__init__(id_player)
        self.behavior = "randKill"

    def play(self, players: List[Player]):
        rd.rand_kill(self, players)


class RandFullPlayer(Player):
    def __init__(self, id_player: int):
        super().__init__(id_player)
        self.behavior = "randFull"

    def play(self, players: List[Player]):
        rd.rand_act(self, players)


class IdlePlayer(Player):
    def __init__(self, id_player: int):
        super().__init__(id_player)
        self.behavior = "idle"

    def play(self, players: List[Player]):  # do nothing
        a = 1
        a += 1


class DetAscPlayer(Player):

    def __init__(self, id_player: int):
        super().__init__(id_player)
        self.behavior = "detAsc"

    def play(self, players: List[Player]):
        det.kill_asc(self, players)


class DetDescPlayer(Player):

    def __init__(self, id_player: int):
        super().__init__(id_player)
        self.behavior = "detDesc"

    def play(self, players: List[Player]):
        det.kill_desc(self, players)


class BestKillPlayer(Player):

    def __init__(self, id_player: int):
        super().__init__(id_player)
        self.behavior = "bestKill"

    def play(self, players: List[Player]):
        det.kill_best(self, players)
