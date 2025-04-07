from src.longest_word.game import Game

# tests/test_game.py
class TestGame:
    def setup_method(self):
        self.game = Game()
        self.grid = self.game.grid

    def test_game_initialization(self):
        grid = self.grid
        # verify
        assert isinstance(grid, list)
        assert len(grid) == 9
        for letter in grid:
            assert letter == letter.upper()
        # teardown

    def test_empty_word_invalid(self):
        valid = self.game.is_valid("")
        assert valid == False

    def test_is_valid(self):
        game = self.game
        game.grid = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        valid = game.is_valid("abc")
        assert valid == True

    def test_is_invalid(self):
        game = self.game
        game.grid = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        valid = game.is_valid("xyz")
        assert valid == False
