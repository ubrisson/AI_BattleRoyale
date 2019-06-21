class Board:
    def __init__(self, game):
        self.board = [player.stats() for player in game.players]

    def get_player(self, k):
        return self.board[k]

    def set_player(self, k, player):
        self.board[k] = player

    def alive_players(self):
        sortie = [player["id"] for player in self.board if player["alive"]]
        return sortie

    def refresh_board(self, game):
        self.board = [player.stats for player in game.players]
