
class MementoTracker():

    def __init__(self):
        self._mementos = []
        self._popped_mementos = []  # for redo

    def saveState(self, turnNumber, currPlayer, board):
        """Save the state of the game."""
        memento = Memento(turnNumber, currPlayer, board)
        self._mementos.append(memento)

        # when we save a new state, we can no longer redo
        self._popped_mementos = []

    def undo(self):
        """Undo."""
        if len(self._mementos) <= 1:
            return None

        curr_state = self._mementos.pop()
        self._popped_mementos.append(curr_state)

        last_state = self._mementos[-1]
        return last_state

    def redo(self):
        """Redo."""
        if len(self._popped_mementos) == 0:
            return None

        memento = self._popped_mementos.pop()
        self._mementos.append(memento)
        return memento


class Memento():
    def __init__(self, turnNumber, currPlayer, board):
        self._turnNumber = turnNumber
        self._currPlayer = currPlayer
        self._board = board.makeCopy()

    def getTurnNumber(self):
        return self._turnNumber

    def getCurrPlayer(self):
        return self._currPlayer

    def getBoard(self):
        return self._board