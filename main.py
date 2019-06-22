from src.engine import *

result = []

for i in range(10):
    game = Game(100)
    result.append(game.run_game())

for name, member in Behavior.__members__.items():
    print(f" {name} : {result.count(member)} ")
