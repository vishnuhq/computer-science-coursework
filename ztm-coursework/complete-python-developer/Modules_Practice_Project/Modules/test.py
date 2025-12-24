import unittest
import random_game2


class TestMain(unittest.TestCase):
    def test_right_guess(self):
        result = random_game2.guessing_game(6, 6)
        self.assertTrue(result)

    def test_wrong_guess(self):
        result = random_game2.guessing_game(1, 6)
        self.assertFalse(result)

    def test_wrong_number(self):
        result = random_game2.guessing_game(11, 6)
        self.assertFalse(result)

    def test_wrong_type(self):
        result = random_game2.guessing_game('66', 6)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
