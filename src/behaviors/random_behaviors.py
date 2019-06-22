from random import randrange, randint
from typing import List

from src import player


def rand_kill(me: 'player.Player', targets: List['player.Player']):
    target = targets[randrange(len(targets))]
    while target is me:
        target = targets[randrange(len(targets))]
    target.killed = True
    me.kills += 1


def rand_act(me: 'player.Player', targets: List['player.Player'], willpower: int = 50):
    if randint(0, 100) <= willpower:
        rand_kill(me, targets)
