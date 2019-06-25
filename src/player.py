from abc import ABC, abstractmethod
from typing import List

from src.behaviors.behaviors import Behavior


class Player(ABC):
    __last_id  = 0
    def __init__(self):
        self.id: int = Player.__last_id
        Player.__last_id += 1
        self.kills: int = 0
        self.alive: bool = True
        self.killed: bool = False
        self.behavior: Behavior = Behavior.IDLE

    @abstractmethod
    def play(self, players: List["Player"]):
        pass

    def die(self):
        self.alive = not self.killed

    def __repr__(self):
        return f" {self.id} : {self.kills}"

class IdlePlayer(Player):
    def __init__(self):
        super().__init__()
        self.behavior = Behavior.IDLE

    def play(self, players: List[Player]):  # do nothing
        pass
