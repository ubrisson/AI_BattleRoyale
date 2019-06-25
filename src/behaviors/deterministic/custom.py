from typing import List

from src.behaviors.behaviors import Behavior
from src.player import Player


class CustomPlayer(Player):

    def __init__(self):
        super().__init__()
        self.behavior = Behavior.CUSTOM

    def play(self, players: List[Player]):
        kill(self, players)


def kill(me: 'Player', targets: List['Player']):
    if len(targets) > 10 and game_isnt_idle(targets):
        pass
    else:
        cont = True
        for x in targets:
            if x.behavior == Behavior.KILLBEST:
                target = x
                cont = False
                break
        if cont:
            for x in targets:
                if x.behavior == Behavior.RANDKILL:
                    target = x
                    cont = False
                    break
        if cont:
            for x in targets:
                if x.behavior == Behavior.DETDESC and x.behavior == Behavior.DETASC:
                    target = x
                    cont = False
                    break
        if cont:
            for x in targets:
                if x.id is not me.id:
                    target = x
                    cont = False
                    break
        if not cont:
            target.killed = True
            me.kills += 1


def game_isnt_idle(targets):
    for player in targets:
        if player.behavior != Behavior.IDLE and player.behavior != Behavior.CUSTOM:
            return True
    return False
