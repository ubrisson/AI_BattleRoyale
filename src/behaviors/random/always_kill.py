from random import randrange, randint
from typing import List

from src import player
from src.behaviors.behaviors import Behavior
from src.player import Player

class RandKillPlayer(Player):
    def __init__(self, id_player: int):
        super().__init__(id_player)
        self.behavior = Behavior.RANDKILL

    def play(self, players: List[Player]):
        self.rand_kill(players)

    def rand_kill(self: 'player.Player', targets: List['player.Player']):
        target = targets[randrange(len(targets))]
        while target is self:
            target = targets[randrange(len(targets))]
        target.killed = True
        self.kills += 1