from Board import Board
from HumanPlayer import HumanPlayer
from Memento import MementoTracker
from Player import Player
from ComputerPlayer import ComputerPlayer
from Exceptions import GameEndedError

class Santorini():
    def __init__(self, white_type=Player.HUMAN, blue_type=Player.HUMAN, 
                    enable_undo="off", enable_score_display="off"):
        # game board
        self._board = Board()
        # two players
        if(white_type == Player.HUMAN):
            self._whitePlayer = HumanPlayer(Player.WHITE, self._board)
        else:
            self._whitePlayer = ComputerPlayer(Player.WHITE, self._board, white_type)
        if(blue_type == Player.HUMAN):
            self._bluePlayer = HumanPlayer(Player.BLUE, self._board)
        else:
            self._bluePlayer = ComputerPlayer(Player.BLUE, self._board, blue_type)
        # current state of game
        self._turnNumber = 1
        self._currPlayer = self._whitePlayer
        # settings
        if enable_undo == "on":
            self._enable_undo = True
            self._mementoTracker = MementoTracker()
        else:
            self._enable_undo = False

        if enable_score_display == "on":
            self._enable_score_display = True
        else:
            self._enable_score_display = False
            
        

    def _getWinner(self):
        """Return the player that has won, or None if no one has won."""
        if self._whitePlayer.hasWon():
            return Player.WHITE
        elif self._bluePlayer.hasWon():
            return Player.BLUE
        else:
            return None

    def _save(self):
        """Save state of game."""
        self._mementoTracker.saveState(self._turnNumber, self._currPlayer, self._board)

    def _performUndo(self):
        """Undo past turn."""
        memento = self._mementoTracker.undo()
        if memento is None:
            return
        # update states
        self._turnNumber = memento.getTurnNumber()
        self._currPlayer = memento.getCurrPlayer()
        self._board.board = memento.getBoard().makeCopyOfBoardArr()
        self._board.workers = memento.getBoard().makeCopyOfWorkers()

    def _performRedo(self):
        """Redo a turn that was undone."""
        memento = self._mementoTracker.redo()
        if memento is None:
            return
        # update states
        self._turnNumber = memento.getTurnNumber()
        self._currPlayer = memento.getCurrPlayer()
        self._board.board = memento.getBoard().makeCopyOfBoardArr()
        self._board.workers = memento.getBoard().makeCopyOfWorkers()

    def playNewTurn(self):
        """Start a new round of game."""
        # first check if anyone has won
        winner = self._getWinner()
        if winner is not None:
            raise GameEndedError(winner)

        # check for undo redo
        if self._enable_undo:
            self._save()
            while True:
                memo_input = input("undo, redo, or next\n")
                if memo_input == "undo":
                    self._performUndo()
                    print(self)
                elif memo_input == "redo":
                    self._performRedo()
                    print(self)
                elif memo_input == "next":
                    break
        

        # play a new turn
        self._currPlayer.play()
        
        # update turn info to prepare for next turn
        self._turnNumber += 1
        if(self._currPlayer == self._bluePlayer):
            self._currPlayer = self._whitePlayer
        else:
            self._currPlayer = self._bluePlayer


    def __str__(self):
        result = str(self._board)
        curr = self._currPlayer.getColor()
        if curr == Player.WHITE:
            curr += " (AB)"
        else:
            curr += " (YZ)"
        
        if self._enable_score_display:
            heightScore = self._currPlayer._computeHeightScore()
            centerScore = self._currPlayer._computeCenterScore()
            distanceScore = self._currPlayer._computeDistanceScore()
            curr += f", ({heightScore}, {centerScore}, {distanceScore})"
            
        result += f"Turn: {self._turnNumber}, {curr}"
        return result