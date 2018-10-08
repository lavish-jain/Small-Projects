from GUI import ROCK, PAPER, SCISSOR
import random

class RockPaperScissors:

    def __init__(self, user_choice):
        RockPaperScissors.user_score = 0
        RockPaperScissors.computer_score = 0
        self.user = user_choice
        self.computer = self.__choose_computer_move()
        self.winner = self.__find_winner()

    def __choose_computer_move(self):
        return random.choice([ROCK, PAPER, SCISSOR])

    def __find_winner(self):
        if (self.user == ROCK and self.computer == SCISSOR) or (self.user == SCISSOR and self.computer == PAPER) or (self.user == PAPER and self.computer == ROCK):
            RockPaperScissors.user_score += 1
            return "YOU"
        elif self.user == self.computer:
            return "NO ONE (ITS A TIE)!"
        else:
            RockPaperScissors.computer_score += 1
            return "COMPUTER"