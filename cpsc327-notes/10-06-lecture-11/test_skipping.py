import unittest
import sys


class SkipTests(unittest.TestCase):

    @unittest.expectedFailure
    def test_fails(self):
        self.assertEqual(False, True)

    @unittest.skip("The code for this test is not yet implemented")
    def test_skip(self):
        self.assertEqual(False, True)

    @unittest.skipIf(sys.version_info.minor == 8, "broken on 3.8")
    def test_skipif(self):
        self.assertEqual(False, True)

    @unittest.skipUnless(
        sys.platform.startswith("windows"), "broken unless on windows"
    )
    def test_skipunless(self):
        self.assertEqual(False, True)

    def test_passing(self):
        self.assertEqual(True, True)


if __name__ == "__main__":
    unittest.main()