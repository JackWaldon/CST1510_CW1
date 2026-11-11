import random
def get_computer_choice():
    number = random.randint(0,2)
    if number == 0:
        return "rock"
    elif number == 1:
        return "paper"
    else:
        return "scissors"

def decide_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw"
    elif (computer_choice == "rock" and user_choice == "paper") or (computer_choice == "paper" and user_choice == "scissors") or (computer_choice == "scissors" and user_choice == "rock"):
        return "Player has won!!"
    else:
        return "Computer has won!!"

user_choice = input('pick: rock, paper or scissors -- ')
computer_choice = (get_computer_choice())
print(computer_choice)
winner = decide_winner(user_choice, computer_choice)

print(winner)
