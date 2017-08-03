"""dice game"""
from random import randint
from time import sleep
def get_user_guess():
  user_guess = input("Guess a number: ")
  return int(user_guess)

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = 2*number_of_sides
  print("The maximum value is " + str(max_val))
  sleep(1)
  user_guess = get_user_guess()
  if (user_guess > max_val):
    print("invalid guess!")
    return
  else:
    print("Rolling...")
    sleep(2)
    print("The first roll is %d" % first_roll)
    sleep(1)
    print("The second roll is %d" % second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print("Result...")
    sleep(1)
    if (user_guess > total_roll):
      print("The player won!")
      return
    else:
      print("You lost!")
      return
