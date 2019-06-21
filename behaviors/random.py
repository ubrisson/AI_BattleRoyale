from random import randrange


class Random:

    def play(self, targets):
        target = randrange(len(targets))
        # print(targets[target])
        return targets[target]
