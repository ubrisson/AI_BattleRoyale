from typing import List

from src.behaviors.behaviors import Behavior
from src.player import Player


class DetAscPlayer(Player):

    def __init__(self):
        super().__init__()
        self.behavior = Behavior.DETASC

    def play(self, players: List[Player]):
        self.kill_asc(players)

    def kill_asc(self, targets: List['Player']):
        my_index = targets.index(self)
        target = targets[my_index + 1] if my_index != len(targets) - 1 else targets[0]
        while target is self:  # cas ou targets[0] is me
            i = 1
            target = targets[i + 1]
        target.killed = True
        self.kills += 1
