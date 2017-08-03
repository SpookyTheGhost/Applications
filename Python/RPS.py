"""Game of Rock, Paper, Scissors"""
from random import randint
from time import sleep
options = ["R", "P", "S"]
WIN = "You won!"
LOSE = "You lost!"
temp = WIN
def decide_winner(user_choice, computer_choice):
  print (computer_choice)
  sleep(1)
  print (user_choice)
  sleep(1)
  user_choice_index = options.index(user_choice)
  computerChoice = options.index(computer_choice)
  if (user_choice_index > 2 or computerChoice > 2):
    print("INVALID SELECTION")
    return
  
  if (user_choice_index == computerChoice):
		print("TIE!")
  elif (user_choice_index == 0 and computerChoice == 2):
    print(WIN)
  elif (user_choice_index == 2 and computerChoice == 1):
    print(WIN)
  elif (user_choice_index == 1 and computerChoice == 0):
    print(WIN)
  else:
    print(LOSE)

def play_RPS():
  print("Welcome to Rock, Paper, Scissors")
  user_choice = input("Select R for Rock, P for Paper, or S for Scissors:")
  user_choice = user_choice.upper()
  computer_choice = options[randint(0, len(options) - 1)]
  decide_winner(user_choice, computer_choice)

play_RPS()
