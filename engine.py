from copy import deepcopy

from environnement import Board
from player import *


class Game:
    def __init__(self, nb_players):
        self.players = self.initPlayers(nb_players)
        self.b = Board(self)

    @staticmethod
    def initPlayers(nb_players):
        stats = []
        for i in range(nb_players):
            player = RandomPlayer("R", i)
            stats.insert(i, player)
        return stats

    def runGame(self):
        alive = self.b.alive_players()
        while len(alive) > 1:
            self.play()
            alive = self.b.alive_players()
        return self.endOfGame()

    def endOfGame(self):
        print(self.b.alive_players())
        print(len(self.b.alive_players()))

    def play(self):
        print("nb restants : " + str(len(self.b.alive_players())))
        aux = deepcopy(self.b)
        for player in self.players:
            killed = player.play(self.b)
            self.kill(killed)
            aux.board[killed]["alive"] = False
        self.b = aux
        print("nb restants : " + str(len(self.b.alive_players())))

    def kill(self, id_player):
        self.players[id_player].alive = False
