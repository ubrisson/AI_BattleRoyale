from src.engine import *

result = []

for i in range(10000):
    game = Game(100)
    result.append(game.run_game())

print(f" detAsc  : {result.count('detAsc')}")
print(f" detDesc : {result.count('detDesc')}")
print(f" randFull  : {result.count('randFull')}")
print(f" randKill  : {result.count('randKill')}")
print(f" idle  : {result.count('idle')}")
print(f" No Winner  : {result.count('No Winner')}")
