import unittest
from unittest.mock import Mock, patch, call

from Exceptions import CannotBuildError, CannotMoveError, NotValidWorkerError, NotYourWorkerError
from Board import Board
from Player import Player
from Worker import Worker

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.white_player = Player("white", self.board)
        self.blue_player = Player("blue", self.board)
    
    def test_selectWorker(self):
        with self.assertRaises(NotValidWorkerError):
            self.white_player._selectWorker("a")
        with self.assertRaises(NotValidWorkerError):
            self.blue_player._selectWorker("worker_y")

        with self.assertRaises(NotYourWorkerError):
            self.white_player._selectWorker("Y")
        with self.assertRaises(NotYourWorkerError):
            self.white_player._selectWorker("Z")

        with self.assertRaises(NotYourWorkerError):
            self.blue_player._selectWorker("A")
        with self.assertRaises(NotYourWorkerError):
            self.blue_player._selectWorker("B")

    def test_distanceScore(self):
        self.assertEqual(self.white_player._computeDistanceScore(), 4)

        self.white_player._selectWorker("A")
        self.white_player._moveWorker("nw")
        self.assertEqual(self.blue_player._computeDistanceScore(), 5)

        self.blue_player._selectWorker("Y")
        self.blue_player._moveWorker("e")
        self.assertEqual(self.white_player._computeDistanceScore(), 5)

    def test_centerScore(self):
        self.assertEqual(self.white_player._computeCenterScore(), 2)

        self.white_player._selectWorker("A")
        self.white_player._moveWorker("nw")
        self.assertEqual(self.blue_player._computeCenterScore(), 2)

        self.blue_player._selectWorker("Y")
        self.blue_player._moveWorker("e")
        self.assertEqual(self.white_player._computeCenterScore(), 1)


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
    
    def test_move(self):
        self.board.moveWorker("Y", "e")
        with self.assertRaises(CannotMoveError):
            self.board.moveWorker("Y", "e")

    def test_build(self):
        self.board.moveWorker("Y", "e")
        with self.assertRaises(CannotBuildError):
            self.board.build("Y", "e")

        self.board.moveWorker("A", "n")
        self.board.build("A", "n")
        self.assertEqual(self.board._getHeightInCell(1,1), 1)

    def test_build_heightLimit(self):
        self.board.board[1][1] = 4
        self.board.moveWorker("Y", "n")
        with self.assertRaises(CannotBuildError):
            self.board.build("Y", "s")

    def test_distance_between(self):
        self.board.moveWorker("A", "nw")
        self.assertEqual(self.board.getDistanceBetweenWorkers("A", "Y"), 1)
        self.assertEqual(self.board.getDistanceBetweenWorkers("A", "Z"), 3)



class TestWorker(unittest.TestCase):

    def test_distanceFrom(self):
        worker = Worker("A", 0, 2)
        self.assertEqual(worker.getDistanceFrom(0, 2), 0)
        self.assertEqual(worker.getDistanceFrom(1, 1), 1)
        self.assertEqual(worker.getDistanceFrom(1, 0), 2)
