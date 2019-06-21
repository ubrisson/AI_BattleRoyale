from typing import List

from src.player import RandomPlayer, Player


class Game:
    def __init__(self, nb_players: int):
        self.players: List[Player] = self.init_players(nb_players)
        print(self.players)

    @staticmethod
    def init_players(nb_players: int) -> List[Player]:
        players = []
        for i in range(nb_players):
            player = RandomPlayer("R", i)
            players.append(player)
        return players

    def run_game(self) -> None:
        alive = self.alive_players()
        while len(alive) > 1:
            self.play()
            alive = self.alive_players()
        return self.end_game()

    def end_game(self) -> None:
        print(self.alive_players())
        print(len(self.alive_players()))

    def play(self) -> None:
        alive_players = self.alive_players()
        print(f"nb restants : {len(alive_players)}")
        for player in alive_players:
            player.play(alive_players)
        self.resolve()

    def resolve(self) -> None:
        for player in self.players:
            player.die()

    def alive_players(self) -> List[Player]:
        return [player for player in self.players if player.alive]
