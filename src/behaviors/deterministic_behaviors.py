from typing import List

from src import player


def kill_asc(me: 'player.Player', targets: List['player.Player']):
    my_index = targets.index(me)
    target = targets[my_index + 1] if my_index != len(targets) - 1 else targets[0]
    target.killed = True
    me.kills += 1


def kill_desc(me: 'player.Player', targets: List['player.Player']):
    my_index = targets.index(me)
    target = targets[my_index - 1] if my_index != 0 else targets[len(targets) - 1]
    target.killed = True
    me.kills += 1
