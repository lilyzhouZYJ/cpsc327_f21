from Exceptions import CannotMoveError, CannotBuildError
from Worker import Worker

class Board():
    
    def __init__(self):
        self.board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        workerA = Worker("A", 3, 1)
        workerB = Worker("B", 1, 3)
        workerY = Worker("Y", 1, 1)
        workerZ = Worker("Z", 3, 3)
        self.workers = {
            "A": workerA,
            "B": workerB,
            "Y": workerY,
            "Z": workerZ
        }


    def getNewCell(self, row, col, dir):
        """Given original row and col, find new row and col after moving in the given direction."""
        if dir == 'n':
            row -= 1
        elif dir == 'ne':
            row -= 1
            col += 1
        elif dir == 'e':
            col += 1
        elif dir == 'se':
            row += 1
            col += 1
        elif dir == 's':
            row += 1
        elif dir == 'sw':
            row += 1
            col -= 1
        elif dir == 'w':
            col -= 1
        elif dir == 'nw':
            row -= 1
            col -= 1
        
        return row, col

    def moveWorker(self, worker, dir):
        """Move the given worker in the given direction."""        
        # current height of worker
        worker = self.workers[worker]
        height = self.board[worker.row][worker.col]

        # row and col of target cell)
        row, col = self.getNewCell(worker.row, worker.col, dir)
        
        # exceeds board
        if row >= 5 or row < 0 or col >= 5 or col < 0:
            raise CannotMoveError()

        # destination is occupied by another worker
        if self._getWorkerInCell(row, col) != None:
            raise CannotMoveError()

        # destination is too high
        if self.board[row][col] - height > 1:
            raise CannotMoveError()

        worker.move(row, col)

    def moveWorkerToCell(self, worker, row, col):
        """Move the worker to the given cell."""
        self.workers[worker].move(row, col)

    def checkValidBuild(self, row, col):
        """Check if we can build at the given cell."""
        # exceeds board
        if row >= 5 or row < 0 or col >= 5 or col < 0:
            raise CannotBuildError()

        # destination is occupied by another worker
        if self._getWorkerInCell(row, col) != None:
            raise CannotBuildError()

        # destination already has 4 levels
        if self._getHeightInCell(row, col) == 4:
            raise CannotBuildError()

    def build(self, worker, dir):
        """Build in the given direction."""        
        # row and col of the target cell
        worker = self.workers[worker]
        row, col = self.getNewCell(worker.row, worker.col, dir)
        
        # check if we can build
        self.checkValidBuild(row, col)

        # build:
        self.board[row][col] += 1


    def _getWorkerInCell(self, row, col):
        """Return the worker in the given cell, or None."""
        for worker in self.workers.values():
            if worker.occupyCell(row, col):
                return worker
        return None

    def _getHeightInCell(self, row, col):
        """Return the height of the given cell."""
        return self.board[row][col]

    def getHeightOfWorker(self, worker):
        """Return the height of where the given worker is."""
        worker = self.workers[worker]
        return self._getHeightInCell(worker.row, worker.col)

    def getCellOfWorker(self, worker):
        """Return the row and col of the given worker."""
        worker = self.workers[worker]
        return worker.row, worker.col

    def getDistanceBetweenWorkers(self, worker1, worker2):
        """Compute the distance between the two workers."""
        worker1 = self.workers[worker1]
        worker2 = self.workers[worker2]
        return worker1.getDistanceFrom(worker2.row, worker2.col)

    def getDistanceOfWorkerFromCenter(self, worker):
        """Compute the distance of worker from the center of board."""
        worker = self.workers[worker]
        return worker.getDistanceFrom(2, 2)

    def __str__(self):
        "Format how the board is to be printed."
        result = '+--+--+--+--+--+\n'
        for r, row in enumerate(self.board):
            result += '|'
            for c, elt in enumerate(row):
                result += str(elt)
                worker = self._getWorkerInCell(r, c)
                if worker != None:
                    result += worker.get_name()
                else:
                    result += ' '
                result += '|'
            result += "\n+--+--+--+--+--+\n"
        return result

    def makeCopyOfBoardArr(self):
        board_array = []
        for row in self.board:
            new_row = []
            for elt in row:
                new_row.append(elt)
            board_array.append(new_row)
        return board_array

    def makeCopyOfWorkers(self):
        workerA = self.workers["A"].makeCopy()
        workerB = self.workers["B"].makeCopy()
        workerY = self.workers["Y"].makeCopy()
        workerZ = self.workers["Z"].makeCopy()
        workers = {
            "A": workerA,
            "B": workerB,
            "Y": workerY,
            "Z": workerZ
        }
        return workers

    def makeCopy(self):
        newBoard = Board()
        newBoard.board = self.makeCopyOfBoardArr()
        newBoard.workers = self.makeCopyOfWorkers()
        return newBoard