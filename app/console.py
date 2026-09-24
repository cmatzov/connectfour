from app.game import Game
from app.player import Player
from app.grid import Grid

class Console:
    def start(self):
        players = self._create_players()
        grid = self._create_grid()
        game = Game(players, grid)
        
        self._play_game(game)

    def _set_number_of_players(self) -> int:
        try:
            number_of_players = int(input("Number of players: 2-4 \n"))
        except ValueError:
            number_of_players = 2
        if not number_of_players <= 4:
            number_of_players = 2
        return number_of_players

    def _create_players(self):
        self.number_of_players = self._set_number_of_players()
        pieces = ["X", "O", "*", "="]
        players = []

        for n in range(1, self.number_of_players + 1):
            username = input(f"Player{n} please choose a username: ")
            if len(username) < 1:
                print("The game will chose a username for you!")
                username = f"Player{n}"
            piece = pieces[n - 1]
            players.append(Player(username, piece))
        return players

    def _create_grid(self):
        rows = columns = 5
        try:
            rows = int(input("Player1 must choose board dimensions, first the number of rows: "))
            columns = int(input("Then columns: "))
        except ValueError:
            pass

        return Grid(rows, columns)

    def _play_game(self, game):
        while not game.is_over:
            self._play_turn(game)

        if self.winner:
            print(f"{self.winner.username} wins!")
        else:
            print("Game ended in a Draw")

    def _play_turn(self, game):
        column = 0
        try:
            column = int(input(f"{game.current_player.username}, choose a column where to place the piece: "))
        except ValueError:
            pass

        result = game.play(column)

        if result == "Illegal Move":
            print("Illegal Move")