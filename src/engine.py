
from typing import List

from src.behaviors.behaviors import Behavior, rand_behavior
from src.player import Player, new_player


class Game:
    def __init__(self, nb_players: int):
        self.players: List[Player] = self.init_players(nb_players)

    @staticmethod
    def init_players(nb_players: int) -> List[Player]:
        players = []
        for i in range(nb_players):
            behavior = rand_behavior()
            players.append(new_player(behavior, i))
        return players

    def run_game(self) -> Behavior:
        alive = self.alive_players()
        while len(alive) > 5:
            self.play()
            alive = self.alive_players()
        return self.end_game()

    def end_game(self) -> Behavior:
        if len(self.alive_players()) != 0:
            return self.alive_players()[0].behavior
        else:
            return Behavior.DEFAULT

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
        return [player for player in self.players if player.alive]
