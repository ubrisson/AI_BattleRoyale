from environnement import Board
from player import *


class Game:
    def __init__(self, nb_players):
        self.players = self.initPlayers(nb_players)
        self.board = Board(self)
        print(self.board.board)

    @staticmethod
    def initPlayers(nb_players):
        stats = []
        for i in range(nb_players):
            player = RandomPlayer("R", i)
            stats.insert(i, player)
        return stats

    def runGame(self):
        alive = self.board.alive_players()
        while len(alive) > 1:
            self.play()
            alive = self.board.alive_players()
        return self.endOfGame()

    def endOfGame(self):
        print(self.board.alive_players())
        print(len(self.board.alive_players()))

    def play(self):
        print(f"nb restants : {len(self.board.alive_players())}")
        for player in self.players:
            killed = player.play(self.board)
            if killed is None:
                continue
            self.kill(killed)
        self.board.refresh_board(self.players)
        print(f"nb restants : {len(self.board.alive_players())}")

    def kill(self, id_player):
        self.players[id_player].alive = False
