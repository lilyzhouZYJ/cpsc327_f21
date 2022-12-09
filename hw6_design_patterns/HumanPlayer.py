from Player import Player
from Exceptions import CannotBuildError, CannotMoveError, NotValidDirectionError, NotValidWorkerError, NotYourWorkerError

class HumanPlayer(Player):

    def _selectDirAndBuild(self):
        while True:
            try:
                build_dir = input("Select a direction to build (n, ne, e, se, s, sw, w, nw)\n")
                self._build(build_dir)
            except NotValidDirectionError:
                print("Not a valid direction")
            except CannotBuildError:
                print("Cannot build " + build_dir)
            else:
                break

    def _selectWorkerAndMove(self):
        # select worker
        while True:
            try:
                worker = input("Select a worker to move\n")
                self._selectWorker(worker)
            except NotValidWorkerError:
                print("Not a valid worker")
            except NotYourWorkerError:
                print("That is not your worker")
            else:
                break

        # select direction to move
        while True:
            try:
                move_dir = input("Select a direction to move (n, ne, e, se, s, sw, w, nw)\n")
                self._moveWorker(move_dir)
            except NotValidDirectionError:
                print("Not a valid direction")
            except CannotMoveError:
                print("Cannot move " + move_dir)
            else:
                break