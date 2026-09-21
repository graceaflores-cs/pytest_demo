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


    def test_valid_word_found(self):
        grid = [
            ["A", "B"],
            ["C", "D"]
        ]

        game = Boggle(grid, ["ABC"])

        self.assertIn("ABC", game.getSolution())

    def test_word_not_found(self):
        grid = [
            ["A", "B"],
            ["C", "D"]
        ]

        game = Boggle(grid, ["XYZ"])

        self.assertEqual([], game.getSolution())

    def test_duplicate_dictionary_word(self):
        grid = [
            ["A", "B"],
            ["C", "D"]
        ]

        game = Boggle(grid, ["ABC", "ABC"])

        self.assertIn("ABC", game.getSolution())

    def test_dictionary_with_single_word(self):
        grid = [
            ["A", "B"],
            ["C", "D"]
        ]

        game = Boggle(grid, ["ABC"])

        result = game.getSolution()

        self.assertIsInstance(result, list)

    def test_returns_list(self):
        grid = [
            ["A", "B"],
            ["C", "D"]
        ]

        game = Boggle(grid, ["ABC"])

        self.assertIsInstance(game.getSolution(), list)


if __name__ == "__main__":
    unittest.main()
