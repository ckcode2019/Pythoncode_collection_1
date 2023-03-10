# Name: Charith Kumarasinghe
# Discode id: CHKUMARASINGH#1583

# programing task --

# Write a program that stores a number and the user has to figure it out
# The user can input guesses
# After each guess the program would tell one of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8

def user_guess_number():
  default_number = 8
  user_guess = int(input("Enter a number: "))
  if default_number > user_guess:
    print("The stored number is higher \n")
    user_guess_number()
  elif user_guess > default_number:
    print("The stried number is lower \n")
    user_guess_number()
  else:
    print("You found the number: 8")

user_guess_number()