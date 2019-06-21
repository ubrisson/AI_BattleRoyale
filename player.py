from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from behaviors.random import Random


@dataclass
class PlayerStat:
    id: int
    kills: int
    alive: bool


class Player(ABC):
    def __init__(self, id_player):
        self.id = id_player
        self.kills = 0
        self.alive = True

    @abstractmethod
    def play(self, board):
        pass

    def stats(self) -> PlayerStat:
        return PlayerStat(
            id=self.id,
            kills=self.kills,
            alive=self.alive
        )


class RandomPlayer(Player):

    def __init__(self, behavior, id_player):
        super().__init__(id_player)
        if behavior == "R":
            self.behavior = Random()

    def play(self, board) -> Optional[int]:
        if self.alive:
            targets = board.alive_players()
            return self.behavior.play(targets)
        else:
            return
