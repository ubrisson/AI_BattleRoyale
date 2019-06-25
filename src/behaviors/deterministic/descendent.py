from typing import List

from src.behaviors.behaviors import Behavior
from src.player import Player


class DetDescPlayer(Player):

    def __init__(self):
        super().__init__()
        self.behavior = Behavior.DETDESC

    def play(self, players: List[Player]):
        self.kill_desc(players)

    def kill_desc(self, targets: List['Player']):
        my_index = targets.index(self)
        target = targets[my_index - 1] if my_index != 0 else targets[len(targets) - 1]
        while target is self:  # cas ou targets[len(targets) - 1] is me
            i = 2
            target = targets[len(targets) - i]
        target.killed = True
        self.kills += 1