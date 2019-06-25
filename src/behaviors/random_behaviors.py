from random import randrange, randint
from typing import List

from src import player
from src.behaviors.behaviors import Behavior
from src.player import Player


def rand_kill(me: 'player.Player', targets: List['player.Player']):
    target = targets[randrange(len(targets))]
    while target is me:
        target = targets[randrange(len(targets))]
    target.killed = True
    me.kills += 1


def rand_act(me: 'player.Player', targets: List['player.Player'], willpower: int = 50):
    if randint(0, 100) <= willpower:
        rand_kill(me, targets)


class RandKillPlayer(Player):
    def __init__(self, id_player: int):
        super().__init__(id_player)
        self.behavior = Behavior.RANDKILL

    def play(self, players: List[Player]):
        rand_kill(self, players)


class RandFullPlayer(Player):
    def __init__(self, id_player: int):
        super().__init__(id_player)
        self.behavior = Behavior.RANDFULL

    def play(self, players: List[Player]):
        rand_act(self, players)
