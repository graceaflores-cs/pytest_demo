import unittest
from boggle_solver import Boggle



class TestBoggleSolver(unittest.TestCase):

    def test_empty_dictionary(self):
        grid = [["A"]]
        dictionary = []

        game = Boggle(grid, dictionary)

        self.assertEqual([], game.getSolution())

    def test_empty_grid(self):
        game = Boggle([], ["ABC"])

        self.assertEqual([], game.getSolution())

    def test_one_by_one_grid(self):
        game = Boggle([["A"]], ["ABC"])

        self.assertEqual([], game.getSolution())


if __name__ == "__main__":
    unittest.main()
