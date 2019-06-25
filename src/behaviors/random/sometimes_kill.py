from random import randrange, randint
from typing import List

from src import player
from src.behaviors.behaviors import Behavior
from src.player import Player

class RandActPlayer(Player):
    def __init__(self):
        super().__init__()
        self.behavior = Behavior.RANDFULL

    def play(self, players: List[Player]):
        self.rand_act(players)

    def rand_act(self: 'player.Player', targets: List['player.Player'], willpower: int = 50):
        if randint(0, 100) <= willpower:
            target = targets[randrange(len(targets))]
            while target is self:
                target = targets[randrange(len(targets))]
            target.killed = True
            self.kills += 1
