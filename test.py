from utils import *
import unittest

class TestUtils(unittest.TestCase):
    def testFilterConstructor(self):
        """
        Test that yellows are computed correctly
        """
        expected = Filter(Color.YELLOW,Color.GRAY,Color.GREEN,Color.YELLOW,Color.GREEN)
        actual = Filter.compute(Word("oooll"), Word("llool"))
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
