import sys
from Exceptions import GameEndedError
from Santorini import Santorini
        
class SantoriniCLI():
    def __init__(self, *argv):
        self._santorini = Santorini(*argv)

    def run_game(self):
        """Run the game."""
        while True:
            print(self._santorini)
            try:
                self._santorini.playNewTurn()
            except GameEndedError as end:
                # print victory message
                print(f"{end.getWinner()} has won")
                break



if __name__ == "__main__":
    SantoriniCLI(*sys.argv[1:]).run_game()
    