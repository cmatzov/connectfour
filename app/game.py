from app.player import Player
from app.game_service import GameService

class Game:
    def __init__(self):
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.game_service = None
        self.current_player = None

    def start_game(self):
        self._create_players()
        self._create_grid()
        self._play_game()

    def _create_players(self):
        username = input("Player1 please choose a username: ")
        if len(username) < 1:
            print("The game will chose a username for you!")
            username = "John"
        self.player1.set_username(username)

        username = input("Player2 please choose a username: ")
        if len(username) < 1:
            print("The game will chose a username for you!")
            username = "Doe"
        self.player2.set_username(username)

    def _create_grid(self):
        rows = columns = 5
        try:
            rows = int(input("Player1 must choose board dimensions, first the number of rows: "))
            columns = int(input(("Then columns: ")))
        except ValueError:
            pass

        self.game_service = GameService(rows, columns)

    def _play_game(self):
        self.current_player = self.player1

        while True:
            result = self._play_turn()

            if result == self.current_player.piece:
                print(f"{self.current_player.get_username()} wins!")
                break
                
            self._next_player()

    def _play_turn(self):
        column = 0
        try:
            column = int(input(f"{self.current_player.get_username()}, choose a column where to place the piece: "))
        except ValueError:
            pass

        return self.game_service.place_piece(column, self.current_player.piece)

    def _next_player(self) -> None:
        if self.current_player == self.player1:
            self.current_player = self.player2 
        else:
            self.current_player = self.player1