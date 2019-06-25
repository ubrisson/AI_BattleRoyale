from typing import List

from src.behaviors.behaviors import Behavior
from src.player import Player


class DetAscPlayer(Player):

    def __init__(self, id_player: int):
        super().__init__(id_player)
        self.behavior = Behavior.DETASC

    def play(self, players: List[Player]):
        kill_asc(self, players)


def kill_asc(me: 'Player', targets: List['Player']):
    my_index = targets.index(me)
    target = targets[my_index + 1] if my_index != len(targets) - 1 else targets[0]
    while target is me:  # cas ou targets[0] is me
        i = 1
        target = targets[i + 1]
    target.killed = True
    me.kills += 1


class DetDescPlayer(Player):

    def __init__(self, id_player: int):
        super().__init__(id_player)
        self.behavior = Behavior.DETDESC

    def play(self, players: List[Player]):
        kill_desc(self, players)


def kill_desc(me: 'Player', targets: List['Player']):
    my_index = targets.index(me)
    target = targets[my_index - 1] if my_index != 0 else targets[len(targets) - 1]
    while target is me:  # cas ou targets[len(targets) - 1] is me
        i = 2
        target = targets[len(targets) - i]
    target.killed = True
    me.kills += 1


class KillBestPlayer(Player):

    def __init__(self, id_player: int):
        super().__init__(id_player)
        self.behavior = Behavior.KILLBEST

    def play(self, players: List[Player]):
        kill_best(self, players)


def kill_best(me: 'Player', targets: List['Player']):
    max_kills = 0
    target = None
    # target = max(targets, key=lambda y: y.kills)
    # """
    for x in targets:
        if x.kills >= max_kills and x is not me:
            max_kills = x.kills
            target = x
    # """
    #target = targets[0] if targets[0] is not me else targets[1]
    if target is not None:
        target.killed = True
        me.kills += 1
