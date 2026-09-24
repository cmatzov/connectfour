from app.grid import Grid

class GameService:
    def __init__(self, rows: int, columns: int):
        self.grid: Grid = Grid(rows, columns)

    def _is_legal_move(self, column: int) -> bool:
        return self._validate_column(column) and self._validate_column_not_full(column)

    def _validate_column(self, column: int) -> bool:
        return 0 < column <= self.grid.columns

    def _find_lowest_row(self, column: int) -> int:
        for row in range(self.grid.rows, 0, -1):
            if self.grid.get_cell(row, column) is None:
                return row
        return None

    def _validate_column_not_full(self, column: int) -> bool:
        return self._find_lowest_row(column) is not None

    def place_piece(self, column: int, piece: str):
        if not self._is_legal_move(column):
            return "Illegal Move"

        row = self._find_lowest_row(column)

        self.grid.set_cell(row, column, piece)

        return self._check_win(row, column, piece)

    def _check_win(self, row: int, column: int, piece: str):
        return (
            self._vertical_check(row, column, piece)
            or self._horizontal_check(row, column, piece)
            or self._diagonal_check(row, column, piece)
        )

    def _vertical_check(self, row: int, column: int, piece: str) -> str | None:
        count = 1

        count += self._count_direction(row, column, piece, 1, 0)
        count += self._count_direction(row, column, piece, -1, 0)

        return piece if count >= 4 else None

    def _horizontal_check(self, row: int, column: int, piece: str) -> str | None:
        count = 1

        count += self._count_direction(row, column, piece, 0, 1)
        count += self._count_direction(row, column, piece, 0, -1)

        return piece if count >= 4 else None

    def _diagonal_check(self, row: int, column: int, piece: str) -> str | None:
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


    def _count_direction(self, row: int, column: int, piece: str, row_delta: int, column_delta: int) -> int:
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