import time as t

from src.engine import *

result = []

start = t.time()

# Each 1000 games takes 1.7 sec on my pc
nb_games = 20000
print(f"This shit's gonna run {nb_games} games for {0.0017 * nb_games} sec.")

for i in range(nb_games):
    game = Game(100)
    result.append(game.run_game())
duration = t.time() - start

somme = 0
for name, member in Behavior.__members__.items():
    count = result.count(member)
    somme += count
    print(f" {name} : {count / nb_games * 100} % ")

print(f"There was {nb_games - somme} games without winner.")

print(f"This took {duration} seconds.")
