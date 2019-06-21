from random import randrange
from typing import List

from src import player


def play(me: 'player.Player', targets: List['player.Player']):
    target = targets[randrange(len(targets))]
    while target is me:
        target = targets[randrange(len(targets))]
    target.killed = True
