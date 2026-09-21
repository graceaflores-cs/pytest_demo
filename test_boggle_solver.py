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

def test_empty_rows_grid(self):
        """Frame 14: Grid containing an empty nested list [[]]."""
        game = Boggle([[]], ["ABC"])
        self.assertEqual([], game.getSolution())

    def test_irregular_grid(self):
        """Frame 15: Jagged/irregular grid shapes handle gracefully."""
        grid = [["A", "B", "C"], ["D", "E"]]
        game = Boggle(grid, ["ABC"])
        self.assertEqual([], game.getSolution())

    def test_standard_four_by_four_grid(self):
        """Frame 16: Standard 4x4 Boggle grid."""
        grid = [
            ["A", "B", "C", "D"],
            ["E", "F", "G", "H"],
            ["I", "J", "K", "L"],
            ["M", "N", "O", "P"]
        ]
        game = Boggle(grid, ["ABFE", "MNOP"])
        self.assertIn("ABFE", game.getSolution())

    def test_linear_1x3_grid(self):
        """Frame 17: Horizontal 1x3 linear grid."""
        grid = [["C", "A", "T"]]
        game = Boggle(grid, ["CAT"])
        self.assertIn("CAT", game.getSolution())

    def test_linear_3x1_grid(self):
        """Frame 18: Vertical 3x1 linear grid."""
        grid = [["D"], ["O"], ["G"]]
        game = Boggle(grid, ["DOG"])
        self.assertIn("DOG", game.getSolution())

    def test_qu_tile_handling(self):
        """Frame 19: Grid cell with multi-character tile 'Qu'."""
        grid = [
            ["Qu", "A", "R"],
            ["T",  "Z", "E"],
            ["S",  "T", "S"]
        ]
        game = Boggle(grid, ["QUART", "QUARTZ"])
        solutions = [word.upper() for word in game.getSolution()]
        self.assertIn("QUART", solutions)
        self.assertIn("QUARTZ", solutions)

    def test_st_tile_handling(self):
        """Frame 20: Grid cell with multi-character tile 'St'."""
        grid = [
            ["St", "A", "R"],
            ["E",  "M", "P"],
            ["O",  "N", "S"]
        ]
        game = Boggle(grid, ["STAR"])
        solutions = [word.upper() for word in game.getSolution()]
        self.assertIn("STAR", solutions)

    def test_ie_tile_handling(self):
        """Frame 21: Grid cell with multi-character tile 'Ie'."""
        grid = [
            ["P",  "Ie", "C"],
            ["E",  "S",  "E"],
            ["T",  "A",  "R"]
        ]
        game = Boggle(grid, ["PIECE"])
        solutions = [word.upper() for word in game.getSolution()]
        self.assertIn("PIECE", solutions)

    def test_multiple_special_tiles(self):
        """Frame 22: Grid combining multiple multi-character tiles in one word."""
        grid = [
            ["Qu", "St"],
            ["A",  "Ie"]
        ]
        game = Boggle(grid, ["QUSTIE"])
        solutions = [word.upper() for word in game.getSolution()]
        self.assertIn("QUSTIE", solutions)

    def test_uppercase_grid_lowercase_dict(self):
        """Frame 23: Uppercase grid cells with lowercase dictionary entries."""
        grid = [["A", "B"], ["C", "D"]]
        game = Boggle(grid, ["abc"])
        solutions = [w.lower() for w in game.getSolution()]
        self.assertIn("abc", solutions)

    def test_lowercase_grid_uppercase_dict(self):
        """Frame 24: Lowercase grid cells with uppercase dictionary entries."""
        grid = [["a", "b"], ["c", "d"]]
        game = Boggle(grid, ["ABC"])
        solutions = [w.upper() for w in game.getSolution()]
        self.assertIn("ABC", solutions)

    def test_no_tile_reuse(self):
        """Frame 25: Cells cannot be reused within the same word path."""
        grid = [["A", "B"], ["C", "D"]]
        game = Boggle(grid, ["ABA"])  # Requires reusing cell 'A'
        solutions = [w.upper() for w in game.getSolution()]
        self.assertNotIn("ABA", solutions)

    def test_diagonal_traversal(self):
        """Frame 26: Words formed exclusively via diagonal movements."""
        grid = [
            ["A", "X", "X"],
            ["X", "B", "X"],
            ["X", "X", "C"]
        ]
        game = Boggle(grid, ["ABC"])
        solutions = [w.upper() for w in game.getSolution()]
        self.assertIn("ABC", solutions)

    def test_all_eight_directions(self):
        """Frame 27: Neighbor connections in all 8 cardinal/intercardinal directions."""
        grid = [
            ["A", "B", "C"],
            ["H", "X", "D"],
            ["G", "F", "E"]
        ]
        dict_words = ["XAB", "XBC", "XCD", "XDE", "XEF", "XFG", "XGH", "XHA"]
        game = Boggle(grid, dict_words)
        solutions = [w.upper() for w in game.getSolution()]
        self.assertEqual(len(solutions), 8)

    def test_multiple_paths_same_word(self):
        """Frame 28: Duplicate paths for the same word yield only one solution entry."""
        grid = [
            ["C", "A", "T"],
            ["C", "A", "T"],
            ["X", "Y", "Z"]
        ]
        game = Boggle(grid, ["CAT"])
        self.assertEqual(len(game.getSolution()), 1)

    def test_assignment_sample_grid(self):
        """Frame 29: Complex grid verification matching assignment sample."""
        grid = [
            ["T", "W", "Y", "R"],
            ["E", "N", "P", "H"],
            ["G", "Z", "Qu", "R"],
            ["O", "N", "T", "A"]
        ]
        dictionary = [
            "art", "ego", "gent", "get", "net", "new", "newt", "prat",
            "pry", "qua", "quart", "quartz", "rat", "tar", "tarp",
            "ten", "went", "wet", "arty", "rhr", "not", "quar"
        ]
        game = Boggle(grid, dictionary)
        solutions = [w.lower() for w in game.getSolution()]
        self.assertIn("quart", solutions)
        self.assertIn("quartz", solutions)


if __name__ == "__main__":
    unittest.main()
