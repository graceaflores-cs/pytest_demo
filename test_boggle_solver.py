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

    def test_two_by_two_grid(self):
        game = Boggle([["A", "B"], ["C", "D"]], ["ABC"])
        self.assertIsInstance(game.getSolution(), list)

    def test_three_by_three_grid(self):
        grid = [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"]
        ]

        game = Boggle(grid, ["ABE"])

        self.assertIsInstance(game.getSolution(), list)

    def test_word_too_short(self):
        grid = [
            ["A", "B"],
            ["C", "D"]
        ]

        game = Boggle(grid, ["AB"])

        self.assertNotIn("AB", game.getSolution())

    def test_no_matching_words(self):
        grid = [
            ["A", "B"],
            ["C", "D"]
        ]

        game = Boggle(grid, ["XYZ", "QRS"])

        self.assertEqual([], game.getSolution())

    def test_multiple_dictionary_words(self):
        grid = [
            ["A", "B"],
            ["C", "D"]
        ]

        game = Boggle(grid, ["ABC", "ACD", "XYZ"])

        self.assertIsInstance(game.getSolution(), list)


if __name__ == "__main__":
    unittest.main()
