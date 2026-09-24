from app.grid import Grid
from app.player import Player


class Game:
    def __init__(self, players: list[Player], grid: Grid):
        self.players = players
        self.grid = grid
        self.current_player = players[0]
        self.winner = None
        self.is_over = False
        self.moves = 0

    def play(self, column):
        piece = self.current_player.piece

        if not self._is_legal_move(column):
            return "Illegal Move"

        row = self._find_lowest_row(column)
        self.grid.set_cell(row, column, piece)

        self.moves += 1

        if self._check_win(row, column, piece):
            self.winner = self.current_player
            self.is_over = True
            return piece

        if self.moves == self.grid.rows * self.grid.columns:
            self.is_over = True

        self._next_player()

    def _next_player(self):
        current_player_index = self.players.index(self.current_player)
        next_player_index = (current_player_index + 1) % len(self.players)

        self.current_player = self.players[next_player_index]

    def _is_legal_move(self, column: int) -> bool:
        return (
            self._validate_column(column)
            and self._validate_column_not_full(column)
        )

    def _validate_column(self, column: int) -> bool:
        return 0 < column <= self.grid.columns

    def _validate_column_not_full(self, column: int) -> bool:
        return self.grid.get_cell(1, column) is None

    def _find_lowest_row(self, column: int) -> int | None:
        for row in range(self.grid.rows, 0, -1):
            if self.grid.get_cell(row, column) is None:
                return row

        return None

    def _check_win(self, row: int, column: int, piece: str):
        return (
            self._vertical_check(row, column, piece)
            or self._horizontal_check(row, column, piece)
            or self._diagonal_check(row, column, piece)
        )

    def _vertical_check(self, row, column, piece):
        count = 1
        count += self._count_direction(row, column, piece, 1, 0)
        count += self._count_direction(row, column, piece, -1, 0)

        return piece if count >= 4 else None

    def _horizontal_check(self, row, column, piece):
        count = 1
        count += self._count_direction(row, column, piece, 0, 1)
        count += self._count_direction(row, column, piece, 0, -1)

        return piece if count >= 4 else None

    def _diagonal_check(self, row, column, piece):
        count = 1
        count += self._count_direction(row, column, piece, 1, 1)
        count += self._count_direction(row, column, piece, -1, -1)

        if count >= 4:
            return piece

        count = 1
        count += self._count_direction(row, column, piece, -1, 1)
        count += self._count_direction(row, column, piece, 1, -1)

        if count >= 4:
            return piece

        return None

    def _count_direction(self, row: int, column: int, piece: str, row_delta: int, column_delta: int):
        count = 0
        while True:
            row += row_delta
            column += column_delta
            if not (1 <= row <= self.grid.rows and 1 <= column <= self.grid.columns):
                break
            if self.grid.get_cell(row, column) != piece:
                break
            count += 1
        return count