import random

class Strategy:
    def computeMoveScore(self):
        raise NotImplementedError()

class HeuristicStrategy(Strategy):
    def __init__(self):
        self.c1 = 3
        self.c2 = 2
        self.c3 = 3

    def computeMoveScore(self, heightScore, centerScore, distanceScore):
        """Compute the move score using a heuristic strategy."""
        return self.c1 * heightScore + self.c2 * centerScore + self.c3 * distanceScore

class RandomStrategy(Strategy):
    def computeMoveScore(self, *args):
        return random.random()