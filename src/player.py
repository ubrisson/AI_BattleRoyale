from abc import ABC, abstractmethod
from typing import List

from src.behaviors import fullrandom


class Player(ABC):
    def __init__(self, id_player):
        self.id = id_player
        self.kills = 0
        self.alive = True
        self.killed = False

    @abstractmethod
    def play(self, board):
        pass

    def die(self):
        self.alive = not self.killed

    def __repr__(self):
        return f" {self.id} : {self.kills}"


class RandomPlayer(Player):

    def __init__(self, behavior, id_player):
        super().__init__(id_player)
        if behavior == "R":
            self.behavior = fullrandom.Random()

    def play(self, players: List[Player]):
        self.behavior.play(self, players)
        self.kills += 1
