import time as t
from concurrent.futures import ProcessPoolExecutor, wait

from src.engine import *

result = []


def run_one_game():
    game_par = Game(100)
    return game_par.run_game()


def main():
    start = t.time()
    nb_games = 20000
    print(f"This shit's gonna run {nb_games} games for {0.0017 * nb_games} sec.")
    parallel_results = []
    futures = []
    pool = ProcessPoolExecutor()
    for x in range(nb_games):
        futures.append((pool.submit(run_one_game)))
    print(wait(futures))
    """
    for f in futures:
        parallel_results.append(f.result())
    somme2 = 0
    for name, member in Behavior.__members__.items():
        count2 = parallel_results.count(member)
        somme2 += count2
        print(f" {name} : {count2 / nb_games * 100} % ")
    print(f"There was {nb_games - somme2} games without winner.")
    """
    duration = t.time() - start
    print(f"This took {duration} seconds.")


if __name__ == '__main__':
    main()
