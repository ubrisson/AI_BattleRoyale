from abc import ABC, abstractmethod

from behaviors.random import Random


class Player(ABC):
    def __init__(self, id_player):
        self.id = id_player
        self.kills = 0
        self.alive = True

    @abstractmethod
    def play(self, board):
        pass

    def stats(self):
        return {
            "id": self.id,
            "kills": self.kills,
            "alive": self.alive,
        }


class RandomPlayer(Player):

    def __init__(self, behavior, id_player):
        super().__init__(id_player)
        if behavior == "R":
            self.behavior = Random()

    def play(self, board) -> int:
        targets = board.alive_players()
        return self.behavior.play(targets)
