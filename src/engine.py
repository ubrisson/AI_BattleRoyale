from typing import List, Optional

from src.behaviors.behaviors import Behavior, rand_behavior

# Deterministic
from src.behaviors.deterministic.ascendent import DetAscPlayer
from src.behaviors.deterministic.descendent import DetDescPlayer 
from src.behaviors.deterministic.custom import CustomPlayer
from src.behaviors.deterministic.kill_best import KillBestPlayer 

# Random
from src.behaviors.random.always_kill import RandKillPlayer
from src.behaviors.random.sometimes_kill import RandActPlayer
from src.player import Player, IdlePlayer


class Game:
    def __init__(self, nb_players: int):
        self.players: List[Player] = self.init_players(nb_players)

    def init_players(self, nb_players: int) -> List[Player]:
        for i in range(nb_players):
            behavior = rand_behavior()
            self.add_new_player(behavior)

    def run_game(self) -> Optional[Behavior]:
        alive = self.alive_players()
        while len(alive) > 1 and self.game_isnt_idle(alive):
            self.play()
            alive = self.alive_players()
        return self.end_game()

    def end_game(self) -> Optional[Behavior]:
        if len(self.alive_players()) != 0:
            return self.alive_players()[0].behavior
        else:
            return None

    def play(self) -> None:
        alive_players = self.alive_players()
        # print(f"nb restants : {len(alive_players)}")
        for player in alive_players:
            player.play(alive_players)
        self.resolve()

    def resolve(self) -> None:
        for player in self.players:
            player.die()

    def alive_players(self) -> List[Player]:
        leaderboard = [player for player in self.players if player.alive]
        leaderboard.sort(key=lambda y: y.kills, reverse=True)
        return leaderboard

    def game_isnt_idle(self, alive):
        for player in alive:
            if player.behavior != Behavior.IDLE:
                return True
        return False

    def add_new_player(self,behavior: Behavior) -> Player:
        if behavior == Behavior.RANDFULL:
            self.players.append(RandActPlayer())
        elif behavior == Behavior.RANDKILL:
            self.players.appedn(RandKillPlayer())
        elif behavior == Behavior.IDLE:
            self.players.append(IdlePlayer())
        elif behavior == Behavior.DETASC:
            self.players.append(DetAscPlayer())
        elif behavior == Behavior.DETDESC:
            self.players.append(DetDescPlayer())
        elif behavior == Behavior.KILLBEST:
            self.players.append(KillBestPlayer())
        elif behavior == Behavior.CUSTOM:
            self.players.append(CustomPlayer())
