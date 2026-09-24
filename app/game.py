from app.player import Player
from app.game_service import GameService

class Game:
    def __init__(self):
        self.players = []
        self.pieces = ["X", "O", "*", "="]
        self.game_service = None
        self.current_player = None

    def start_game(self):
        self._create_players()
        self._create_grid()
        self._play_game()

    def _set_number_of_players(self) -> None:
        try:
            number_of_players = int(input("Number of players: 2-4 \n"))
        except ValueError:
            number_of_players = 2
        if not number_of_players <= 4:
            number_of_players = 2
        return number_of_players

    def _create_players(self):
        for n in range(1, self._set_number_of_players() + 1):
            username = input(f"Player{n} please choose a username: ")
            if len(username) < 1:
                print("The game will chose a username for you!")
                username = f"Player{n}"
            piece = self.pieces[n - 1]
            self.players.append(Player(username, piece))

    def _create_grid(self):
        rows = columns = 5
        try:
            rows = int(input("Player1 must choose board dimensions, first the number of rows: "))
            columns = int(input(("Then columns: ")))
        except ValueError:
            pass

        self.game_service = GameService(rows, columns)

    def _play_game(self):
        self.current_player = self.players[0]
        current_player_index = 0

        while True:
            result = self._play_turn()

            if result == self.current_player.piece:
                print(f"{self.current_player.username} wins!")
                break
                
            current_player_index = self._next_player(current_player_index)

    def _play_turn(self):
        column = 0
        try:
            column = int(input(f"{self.current_player.username}, choose a column where to place the piece: "))
        except ValueError:
            pass

        return self.game_service.place_piece(column, self.current_player.piece)

    def _next_player(self, current_player_index: int) -> int:
        current_player_index = (current_player_index + 1) % len(self.players)
        self.current_player = self.players[current_player_index]
        return current_player_index