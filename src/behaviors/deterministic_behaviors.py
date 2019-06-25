from typing import List

from src.behaviors.behaviors import Behavior
from src.player import Player



class DetAscPlayer(Player):

    def __init__(self, id_player: int):
        super().__init__(id_player)
        self.behavior = Behavior.DETASC

    def play(self, players: List[Player]):
        self.kill_asc(self, players)

    def kill_asc(self, targets: List['Player']):
        my_index = targets.index(self)
        target = targets[my_index + 1] if my_index != len(targets) - 1 else targets[0]
        while target is self:  # cas ou targets[0] is me
            i = 1
            target = targets[i + 1]
        target.killed = True
        self.kills += 1


class DetDescPlayer(Player):

    def __init__(self, id_player: int):
        super().__init__(id_player)
        self.behavior = Behavior.DETDESC

    def play(self, players: List[Player]):
        self.kill_desc(self, players)

    def kill_desc(self, targets: List['Player']):
        my_index = targets.index(self)
        target = targets[my_index - 1] if my_index != 0 else targets[len(targets) - 1]
        while target is self:  # cas ou targets[len(targets) - 1] is me
            i = 2
            target = targets[len(targets) - i]
        target.killed = True
        self.kills += 1


class KillBestPlayer(Player):

    def __init__(self, id_player: int):
        super().__init__(id_player)
        self.behavior = Behavior.KILLBESTzoom

    def play(self, players: List[Player]):
        self.kill_best(players)

    def kill_best(self, targets: List['Player']):
        max_kills = 0
        target = None
        # target = max(targets, key=lambda y: y.kills)
        # """
        for x in targets:
            if x.kills >= max_kills and x is not self:
                max_kills = x.kills
                target = x
        # """
        # target = targets[0] if targets[0] is not me else targets[1]
        if target is not None:
            target.killed = True
            self.kills += 1
