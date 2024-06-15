import random

class SnakeAndLadderGame:
    def __init__(self, num_players):
        self.num_players = num_players
        self.players = {f'Player {i+1}': 1 for i in range(num_players)}
        self.players['AI'] = 1  # Adding AI player

    def roll_dice(self):
        return random.randint(1, 6)

    def check_snake_and_ladder(self, position):
        snakes_and_ladders = {14: 7, 27: 9, 40: 3, 43: 18, 54: 34, 66: 36, 76: 55, 89: 64, 99: 69}
        return snakes_and_ladders.get(position, position)

    def is_game_over(self):
        return any(position >= 100 for position in self.players.values())

class MinimaxAI:
    def __init__(self, game):
        self.game = game

    def minimax(self, position, rolls_left, is_maximizing_player):
        if rolls_left == 0 or position >= 100:
            return self.evaluate(position)

        if is_maximizing_player:
            best_score = float('-inf')
            for move in range(1, 7):
                new_position = self.game.check_snake_and_ladder(position + move)
                score = self.minimax(new_position, rolls_left - 1, False)
                best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for move in range(1, 7):
                new_position = self.game.check_snake_and_ladder(position + move)
                score = self.minimax(new_position, rolls_left - 1, True)
                best_score = min(best_score, score)
            return best_score

    def make_move(self):
        return self.game.roll_dice()

    def evaluate(self, position):
        return 100 - position

def main():
    num_players = int(input("Enter the number of human players: "))
    if num_players < 1:
        print("Error: At least one human player is required.")
        return

    game = SnakeAndLadderGame(num_players)
    ai = MinimaxAI(game)

    while not game.is_game_over():
        for player in game.players:
            input("Press any key to roll the dice...")
            if player == 'AI':
                ai_roll = ai.make_move()
                game.players[player] += ai_roll
            else:
                user_roll = game.roll_dice()
                game.players[player] += user_roll

            game.players[player] = game.check_snake_and_ladder(game.players[player])

            print(f"{player} rolled: {user_roll if player != 'AI' else ai_roll}. {player}'s position: {game.players[player]}")
        print()

    winner = max(game.players, key=game.players.get)
    print(f"Game over! {winner} wins!")

if __name__ == "__main__":
    main()
