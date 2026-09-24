class Player:
    def __init__(self, piece: str):
        self._username: str = None
        self.piece = piece

    def get_username(self):
        return self._username

    def set_username(self, username: str) -> None:
        self._username = username