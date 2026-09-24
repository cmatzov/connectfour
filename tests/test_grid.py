from app.grid import Grid
from app.game_service import GameService


# Grid Creation and placement
def test_grid_starts_empty():
    grid = Grid(5, 5)

    assert grid.get_cell(1, 1) is None
    assert grid.get_cell(5, 5) is None


def test_set_cell():
    grid = Grid(5, 5)

    grid.set_cell(5, 1, "X")

    assert grid.get_cell(5, 1) == "X"


def test_set_cell_does_not_change_other_cells():
    grid = Grid(5, 5)

    grid.set_cell(5, 1, "X")

    assert grid.get_cell(5, 2) is None
    assert grid.get_cell(5, 5) is None


# GameService Testing
def test_piece_falls_to_bottom():
    game = GameService(5, 5)

    game.place_piece(1, "X")
    assert game.grid.get_cell(5, 1) == "X"


def test_pieces_stack_in_same_column():
    game = GameService(5, 5)

    game.place_piece(1, "X")
    game.place_piece(1, "O")

    assert game.grid.get_cell(4, 1) == "O"


def test_pieces_in_separate_columns():
    game = GameService(5, 5)

    game.place_piece(1, "X")
    game.place_piece(2, "O")

    assert game.grid.get_cell(5, 1) == "X"
    assert game.grid.get_cell(5, 2) == "O"


def test_full_column():
    game = GameService(5, 5)

    game.place_piece(1, "X")
    game.place_piece(1, "O")
    game.place_piece(1, "X")
    game.place_piece(1, "O")
    game.place_piece(1, "X")

    assert game.grid.get_cell(1, 1) == "X"


def test_piece_cannot_be_placed_in_full_column():
    game = GameService(5, 5)

    game.place_piece(1, "X")
    game.place_piece(1, "O")
    game.place_piece(1, "X")
    game.place_piece(1, "O")
    game.place_piece(1, "X")

    result = game.place_piece(1, "O")

    assert result == "Illegal Move"


def test_invalid_column_left_of_grid():
    game = GameService(5, 5)

    result = game.place_piece(0, "X")

    assert result == "Illegal Move"


def test_invalid_column_right_of_grid():
    game = GameService(5, 5)

    result = game.place_piece(6, "X")

    assert result == "Illegal Move"


def test_negative_column():
    game = GameService(5, 5)

    result = game.place_piece(-1, "X")

    assert result == "Illegal Move"


# --------------------
# Horizontal
# --------------------

def test_horizontal_four_pieces_is_win():
    game = GameService(5, 5)

    game.place_piece(1, "X")
    game.place_piece(2, "X")
    game.place_piece(3, "X")
    winner = game.place_piece(4, "X")

    assert winner == "X"


def test_horizontal_five_pieces_is_win():
    game = GameService(5, 5)

    game.place_piece(1, "X")
    game.place_piece(2, "X")
    game.place_piece(3, "X")
    game.place_piece(4, "X")
    winner = game.place_piece(5, "X")

    assert winner == "X"


def test_horizontal_three_pieces_is_not_win():
    game = GameService(5, 5)

    game.place_piece(1, "X")
    game.place_piece(2, "X")
    winner = game.place_piece(3, "X")

    assert winner is None


def test_horizontal_count_resets_after_opponent():
    game = GameService(5, 5)

    game.place_piece(1, "X")
    game.place_piece(2, "X")
    game.place_piece(3, "O")
    game.place_piece(4, "X")
    winner = game.place_piece(5, "X")

    assert winner is None


def test_horizontal_three_before_opponent_does_not_combine_with_piece_after():
    game = GameService(5, 5)

    game.place_piece(1, "X")
    game.place_piece(2, "X")
    game.place_piece(3, "X")
    game.place_piece(4, "O")
    winner = game.place_piece(5, "X")

    assert winner is None


def test_horizontal_three_after_opponent_is_not_win():
    game = GameService(5, 5)

    game.place_piece(1, "X")
    game.place_piece(2, "O")
    game.place_piece(3, "X")
    game.place_piece(4, "X")
    winner = game.place_piece(5, "X")

    assert winner is None


# --------------------
# Vertical
# --------------------

def test_vertical_four_pieces_is_win():
    game = GameService(5, 5)

    game.place_piece(1, "X")
    game.place_piece(1, "X")
    game.place_piece(1, "X")
    winner = game.place_piece(1, "X")

    assert winner == "X"


def test_vertical_five_pieces_is_win():
    game = GameService(5, 5)

    game.place_piece(1, "X")
    game.place_piece(1, "X")
    game.place_piece(1, "X")
    game.place_piece(1, "X")
    winner = game.place_piece(1, "X")

    assert winner == "X"


def test_vertical_three_pieces_is_not_win():
    game = GameService(5, 5)

    game.place_piece(1, "X")
    game.place_piece(1, "X")
    winner = game.place_piece(1, "X")

    assert winner is None


def test_vertical_count_resets_after_opponent():
    game = GameService(5, 5)

    game.place_piece(1, "X")
    game.place_piece(1, "X")
    game.place_piece(1, "O")
    game.place_piece(1, "X")
    winner = game.place_piece(1, "X")

    assert winner is None


def test_vertical_three_before_opponent_does_not_combine_with_piece_after():
    game = GameService(5, 5)

    game.place_piece(1, "X")
    game.place_piece(1, "X")
    game.place_piece(1, "X")
    game.place_piece(1, "O")
    winner = game.place_piece(1, "X")

    assert winner is None


# --------------------
# Diagonal down-right ↘
# --------------------

def test_diagonal_down_right_four_pieces_is_win():
    game = GameService(5, 5)

    game.place_piece(1, "X")

    game.place_piece(2, "O")
    game.place_piece(2, "X")

    game.place_piece(3, "O")
    game.place_piece(3, "O")
    game.place_piece(3, "X")

    game.place_piece(4, "O")
    game.place_piece(4, "O")
    game.place_piece(4, "O")
    winner = game.place_piece(4, "X")

    assert winner == "X"


def test_diagonal_down_right_interrupted_by_opponent_is_not_win():
    game = GameService(5, 5)

    game.place_piece(1, "X")

    game.place_piece(2, "O")
    game.place_piece(2, "X")

    game.place_piece(3, "O")
    game.place_piece(3, "O")
    game.place_piece(3, "O")

    game.place_piece(4, "O")
    game.place_piece(4, "O")
    game.place_piece(4, "O")
    winner = game.place_piece(4, "X")

    assert winner is None


# --------------------
# Diagonal down-left ↙
# --------------------

def test_diagonal_down_left_four_pieces_is_win():
    game = GameService(5, 5)

    game.place_piece(4, "X")

    game.place_piece(3, "O")
    game.place_piece(3, "X")

    game.place_piece(2, "O")
    game.place_piece(2, "O")
    game.place_piece(2, "X")

    game.place_piece(1, "O")
    game.place_piece(1, "O")
    game.place_piece(1, "O")
    winner = game.place_piece(1, "X")

    assert winner == "X"


def test_diagonal_down_left_interrupted_by_opponent_is_not_win():
    game = GameService(5, 5)

    game.place_piece(4, "X")

    game.place_piece(3, "O")
    game.place_piece(3, "X")

    game.place_piece(2, "O")
    game.place_piece(2, "O")
    game.place_piece(2, "O")

    game.place_piece(1, "O")
    game.place_piece(1, "O")
    game.place_piece(1, "O")
    winner = game.place_piece(1, "X")

    assert winner is None


# --------------------
# Both sides of current piece
# --------------------

def test_horizontal_win_can_be_found_on_both_sides_of_current_piece():
    game = GameService(5, 5)

    game.place_piece(1, "X")
    game.place_piece(2, "X")
    game.place_piece(4, "X")
    game.place_piece(5, "X")
    winner = game.place_piece(3, "X")

    assert winner == "X"


def test_diagonal_win_can_be_found_on_both_sides_of_current_piece():
    game = GameService(5, 5)

    game.place_piece(4, "X")

    game.place_piece(3, "O")
    game.place_piece(3, "X")

    game.place_piece(2, "O")
    game.place_piece(2, "O")

    game.place_piece(1, "O")
    game.place_piece(1, "O")
    game.place_piece(1, "O")
    game.place_piece(1, "X")

    winner = game.place_piece(2, "X")

    assert winner == "X"