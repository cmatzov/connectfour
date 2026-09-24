class Grid:
    def __init__(self, rows, columns):
        self.rows: int = rows
        self.columns: int = columns
        self._grid: list[list[str | None]] = [[None for _ in range(self.columns)] for _ in range(self.rows)]

    def get_cell(self, row: int, column: int) -> str | None:
        return self._grid[row - 1][column - 1]

    def set_cell(self, row: int, column: int, piece: str) -> None:
        self._grid[row - 1][column - 1] = piece