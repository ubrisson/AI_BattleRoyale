from abc import ABC, abstractmethod
from typing import List

from src.behaviors import fullrandom


class Player(ABC):
    def __init__(self, id_player: int):
        self.id: int = id_player
        self.kills: int = 0
        self.alive: bool = True
        self.killed: bool = False

    @abstractmethod
    def play(self, players: List["Player"]):
        pass

    def die(self):
        self.alive = not self.killed

    def __repr__(self):
        return f" {self.id} : {self.kills}"


class RandomPlayer(Player):

    def __init__(self, behavior, id_player: int):
        super().__init__(id_player)
        if behavior == "R":
            self.behavior = fullrandom.Random()

    def play(self, players: List[Player]):
        self.behavior.play(self, players)
        self.kills += 1
