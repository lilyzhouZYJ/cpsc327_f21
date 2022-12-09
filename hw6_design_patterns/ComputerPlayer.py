from Exceptions import GameEndedError
from Player import Player
from Strategy import HeuristicStrategy, RandomStrategy
from random import random, choice

class ComputerPlayer(Player):

    def __init__(self, player_color, board, player_type):
        self._selectedMove = None
        self._selectedBuild = None
        # set up strategy (heuristic or random)
        if player_type == Player.HEURISTIC:
            self._moveScoreStrategy = HeuristicStrategy()
        elif player_type == Player.RANDOM:
            self._moveScoreStrategy = RandomStrategy()
        super().__init__(player_color, board)

    def play(self):
        """Play a round."""
        super().play()
        # print
        print(f"{self._selectedWorker},{self._selectedMove},{self._selectedBuild}")

    def _selectWorkerAndMove(self):
        """Move a worker for the player."""
        best_score = 0
        best_dir = None
        best_worker = None

        workers = Player.PLAYER_WORKERS[self._color]
        for worker in workers:
            new_score, new_dir = self._selectMoveForWorker(worker)
            if best_dir is None:
                best_score = new_score
                best_dir = new_dir
                best_worker = worker
            else:
                if new_dir is not None and new_score > best_score:
                    best_score = new_score
                    best_dir = new_dir
                    best_worker = worker
                elif new_dir is not None and new_score == best_score:
                    if(random() >= 0.5):
                        best_score = new_score
                        best_dir = new_dir
                        best_worker = worker
        
        if best_dir is None:
            # no valid move was found
            # player automatically loses
            if self._color == Player.WHITE:
                color = Player.BLUE
            else:
                color = Player.WHITE
            raise GameEndedError(color)
        else:
            # move!
            self._selectedMove = best_dir
            self._selectWorker(best_worker)
            self._moveWorker(best_dir)

        
    def _selectMoveForWorker(self, worker):
        """Select the best move for the given worker."""
        best_score = 0
        best_dir = None

        # original position of worker
        orig_row, orig_col = self._board.getCellOfWorker(worker)

        for dir in Player.DIRECTIONS:
            try:
                self._board.moveWorker(worker, dir)
            except Exception:
                continue
            else:
                # compute move score
                if self._board.getHeightOfWorker(worker) == 3:
                    # make the score large to ensure it will be chosen
                    move_score = 10000
                else:
                    height_score = self._computeHeightScore()
                    center_score = self._computeCenterScore()
                    distance_score = self._computeDistanceScore()
                    move_score = self._moveScoreStrategy.computeMoveScore(height_score, 
                                                            center_score, distance_score)
                # do we choose current move?
                if move_score > best_score:
                    best_score = move_score
                    best_dir = dir
                elif move_score == best_score:
                    if random() >= 0.5:
                        best_score = move_score
                        best_dir = dir
                # restore worker to original position
                self._board.moveWorkerToCell(worker, orig_row, orig_col)

        return best_score, best_dir

    
    def _selectDirAndBuild(self):
        """Have the selected worker build something, random direction."""
        possible_dir = []
        orig_row, orig_col = self._board.getCellOfWorker(self._selectedWorker)
        for dir in Player.DIRECTIONS:
            row, col = self._board.getNewCell(orig_row, orig_col, dir)
            try:
                self._board.checkValidBuild(row, col)
            except Exception:
                continue
            else:
                possible_dir.append(dir)

        # pick random direction to build
        selected_dir = choice(possible_dir)
        self._build(selected_dir)
        self._selectedBuild = selected_dir