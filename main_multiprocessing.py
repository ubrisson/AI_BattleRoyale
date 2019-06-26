import time
from multiprocessing import Pool
from functools import partial
import itertools
import psutil

from src.engine import *

def run_n_game(no_cpu,n):
    res = []
    for i in range(n):
        game_par = Game(100)
        g = game_par.run_game()
        res.append(g)
    print(f"End process {no_cpu}")
    return res
    

if __name__ == '__main__':
    start = time.time()
    nb_games = 100_000
    # the nb_games should be a multiple of n_cpus
    print(f"This shit's gonna run {nb_games} games for {0.0017 * nb_games} sec.")

    nb_cpus = psutil.cpu_count()
    p = Pool(nb_cpus)
    run = partial(run_n_game, n=nb_games // nb_cpus)
    result = p.map(run, [no_cpu for no_cpu in range(nb_cpus)])
    p.close()
    p.join()
    
    print("End main process")
    somme = 0
    result = list(itertools.chain.from_iterable(result))

    for name, member in Behavior.__members__.items():
        count = result.count(member)
        somme += count
        print(f" {name} : {count / nb_games * 100} % ")

    print(f"There was {nb_games - somme} games without winner.")
    duration = time.time() - start
    print(f"This took {duration} seconds.")