from Exceptions import NotValidWorkerError, NotYourWorkerError, NotValidDirectionError
from Worker import Worker

class Player():
    HUMAN, HEURISTIC, RANDOM = 'human', 'heuristic', 'random'
    WHITE, BLUE = "white", "blue"
    PLAYER_WORKERS = {
        WHITE: ["A", "B"],
        BLUE: ["Y", "Z"]
    }
    DIRECTIONS = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']

    def __init__(self, player_color, board):
        self._color = player_color
        self._board = board
        self._selectedWorker = None

    def getColor(self):
        return self._color

    def hasWon(self):
        """Check if this player has won."""
        for worker in Player.PLAYER_WORKERS[self._color]:
            if self._board.getHeightOfWorker(worker) == 3:
                return True
        return False

    def play(self):
        """Play a round."""
        # the following steps will be implemented by subclasses
        # select a worker and move
        self._selectWorkerAndMove()
        # have the worker build something
        self._selectDirAndBuild()
        
    def _selectWorker(self, worker):
        """Select a worker."""
        if not worker in Worker.WORKERS:
            raise NotValidWorkerError()

        if worker in Player.PLAYER_WORKERS[self._color]:
            self._selectedWorker = worker
        else:
            raise NotYourWorkerError()
    
    def _moveWorker(self, dir):
        """Move the worker on the board."""
        if dir not in Player.DIRECTIONS:
            raise NotValidDirectionError()
        self._board.moveWorker(self._selectedWorker, dir)

    def _build(self, dir):
        """Build in the given direction."""
        if dir not in Player.DIRECTIONS:
            raise NotValidDirectionError()
        self._board.build(self._selectedWorker, dir)

    def _computeHeightScore(self):
        """Compute the height score of the player."""
        workers = Player.PLAYER_WORKERS[self._color]
        return self._board.getHeightOfWorker(workers[0]) + self._board.getHeightOfWorker(workers[1])

    def _computeCenterScore(self):
        """Computer the center score of the player."""
        workers = Player.PLAYER_WORKERS[self._color]
        score1 = 2 - self._board.getDistanceOfWorkerFromCenter(workers[0])
        score2 = 2 - self._board.getDistanceOfWorkerFromCenter(workers[1])
        return score1 + score2

    def _computeDistanceScore(self):
        """Compute the distance score of the player."""
        my_workers = Player.PLAYER_WORKERS[self._color]
        other_workers = (worker for worker in Worker.WORKERS if worker not in my_workers)
        score = 0
        for o_worker in other_workers:
            dist1 = self._board.getDistanceBetweenWorkers(my_workers[0], o_worker)
            dist2 = self._board.getDistanceBetweenWorkers(my_workers[1], o_worker)
            score += min(dist1, dist2)
        return 8 - score
