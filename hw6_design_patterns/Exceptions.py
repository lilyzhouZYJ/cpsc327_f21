class NotValidWorkerError(Exception):    
    """This exception handles user input of invalid worker (anything
    other than A, B, X, Y)."""
    pass

class NotYourWorkerError(Exception):
    """This exception handles user input of opponent's workers."""
    pass

class NotValidDirectionError(Exception):
    """User inputted direction is not valid."""
    pass

class CannotMoveError(Exception):
    """Worker cannot move to the given direction."""
    pass

class CannotBuildError(Exception):
    """Worker cannot build to the given direction."""
    pass

class GameEndedError(Exception):
    """Game has ended."""
    def __init__(self, winner):
        self.winner = winner

    def getWinner(self):
        return self.winner