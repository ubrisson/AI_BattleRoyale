from typing import List

from src.behaviors.behaviors import Behavior
from src.player import Player


class KillBestPlayer(Player):

    def __init__(self):
        super().__init__()
        self.behavior = Behavior.KILLBEST
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
