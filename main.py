import time as t

from src.engine import *

result = []

start = t.time()

# Each 1000 games takes 1.7 sec on my pc
for i in range(1000):
    game = Game(100)
    result.append(game.run_game())
duration = t.time() - start

for name, member in Behavior.__members__.items():
    print(f" {name} : {result.count(member)} ")

print(f"This took {duration} seconds")
