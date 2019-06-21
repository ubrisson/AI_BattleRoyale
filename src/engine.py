from random import randint
from typing import List

from src.player import Player, DetDescPlayer, DetAscPlayer, RandKillPlayer, \
    RandFullPlayer, IdlePlayer, BestKillPlayer


class Game:
    def __init__(self, nb_players: int):
        self.players: List[Player] = self.init_players(nb_players)

    @staticmethod
    def init_players(nb_players: int) -> List[Player]:
        players = []
        for i in range(nb_players):
            r = randint(0, 5)
            if r == 0:
                players.insert(i, DetAscPlayer(i))
            elif r == 1:
                players.insert(i, DetDescPlayer(i))
            elif r == 2:
                players.insert(i, RandFullPlayer(i))
            elif r == 3:
                players.insert(i, RandKillPlayer(i))
            elif r == 4:
                players.insert(i, IdlePlayer(i))
            elif r == 5:
                players.insert(i, BestKillPlayer(i))
        return players

    def run_game(self) -> str:
        alive = self.alive_players()
        while len(alive) > 10:
            self.play()
            alive = self.alive_players()
        return self.end_game()

    def end_game(self) -> str:
        if len(self.alive_players()) != 0:
            return self.alive_players()[0].behavior
        else:
            return "No Winner"

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
