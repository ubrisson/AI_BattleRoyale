from typing import List

from src import player


def kill_asc(me: 'player.Player', targets: List['player.Player']):
    index = me.to_kill + 1 if me.to_kill + 1 != len(targets) else 0
    target = targets[index]
    while target is me:
        index = me.to_kill + 1 if me.to_kill + 1 != len(targets) else 0
        target = targets[index]
    target.killed = True
    me.kills += 1


def kill_desc(me: 'player.Player', targets: List['player.Player']):
    index = me.to_kill - 1 if me.to_kill - 1 != -1 else len(targets) - 1
    target = targets[index]
    while target is me:
        index = me.to_kill - 1 if me.to_kill - 1 != len(targets) else 0
        target = targets[index]
    target.killed = True
    me.kills += 1
