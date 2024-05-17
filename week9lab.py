week9 lab
import random

class RockPaperScissors:
    def __init__(self, num_players):
        self.choices = ['rock', 'paper', 'scissors']
        self.num_players = num_players
        self.scores = {'Player 1': 0, 'Player 2': 0, 'Draws': 0}

    def get_player_choice(self):
        choice = input("Pick one of rock, paper, or scissors: ").lower()
        while choice not in self.choices:
            print("Invalid choice. Please choose from rock, paper, or scissors.")
            choice = input("Pick one of rock, paper, or scissors: ").lower()
        return choice

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, p1, p2):
        if p1 == p2:
            return "It's a draw."
        elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'paper' and p2 == 'rock') or (p1 == 'scissors' and p2 == 'paper'):
            self.scores['Player 1'] += 1
            return "Player 1 wins!"
        else:
            self.scores['Player 2'] += 1
            return "Player 2 wins!"

    def play_round(self):
        if self.num_players == 0:
            p1 = self.get_computer_choice()
            p2 = self.get_computer_choice()
        elif self.num_players == 1:
            p1 = self.get_player_choice()
            p2 = self.get_computer_choice()
        else:
            p1 = self.get_player_choice()
            print("Player 2's turn:")
            p2 = self.get_player_choice()

        result = self.determine_winner(p1, p2)
        print(f"Player 1 chose {p1}, Player 2 chose {p2}. {result}")

    def play_game(self, num_rounds):
        for _ in range(num_rounds):
            self.play_round()
        print(f"Final scores - Player 1: {self.scores['Player 1']}, Player 2: {self.scores['Player 2']}, Draws: {self.scores['Draws']}")

# Main game setup
num_players = int(input("Enter number of human players (0-2): "))
while num_players not in [0, 1, 2]:
    print("Invalid number of players. Please enter 0, 1, or 2.")
    num_players = int(input("Enter number of human players (0-
