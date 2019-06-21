class Board:
    def __init__(self, game):
        self.board = game.players

    def get_player(self, k):
        return self.board[k]

    def set_player(self, k, player):
        self.board[k] = player

    def alive_players(self):
        sortie = [player for player in self.board if player.alive]
        return sortie

    def refresh_board(self, players):
        self.board = players
