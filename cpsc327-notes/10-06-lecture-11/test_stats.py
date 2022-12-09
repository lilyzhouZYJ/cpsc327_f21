from stats import StatsList
import unittest


class TestValidInputs(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")


    def setUp(self):
        print("\nsetUp")
        self.stats = StatsList([1, 2, 2, 3, 3, 4])
        
    def tearDown(self):
        print("tearDown\n")

    def test_mean(self):
        print("test_mean")
        self.assertEqual(self.stats.mean(), 2.5)

    def test_median(self):
        print("test_median")
        self.assertEqual(self.stats.median(), 2.5)
        self.stats.append(4)
        self.assertEqual(self.stats.median(), 3)

    def test_mode(self):
        print("test_mode")
        self.assertEqual(self.stats.mode(), [2, 3])
        self.stats.remove(2)
        self.assertEqual(self.stats.mode(), [3])
        # another test case for some bug that came up


if __name__ == "__main__":
    unittest.main()

    # or run this command:
    # python -m unittest test_stats.py