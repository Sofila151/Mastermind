#File Purpose: Keep Game Functions to check, play again, and take guesses
#Main Contributor to File: Sofia
import random

def play_again():#Nyx Did Version 1
  """This function asks the player if they would like to begin a new game round"""
  answer = input("Do you want to play again? (y/n): ").lower()
  while answer != "y" or answer != "n":
    if answer == "y":
      return True
    elif answer == "n":
      print("Thanks for playing!")
      return False
    else:
      print("Invalid input, type 'y' or 'n' ")
      answer = input("Do you want to play again? (y/n): ").lower()
      
    

def userGuesses():

  print("Enter your color of choice, red, blue, or green in the order of your guess")

  guess1 = input("Guess 1: ").lower()
  guess2 = input("Guess 2: ").lower()
  guess3 = input("Guess 3: ").lower()
  
  userGuess = [guess1,guess2,guess3]
  
  return userGuess

def guess_checker(colors, userGuess):

  black_peg = 0
  grey_peg = 0
  white_peg = 0

  for num in range(3):
    
    playerGuess = userGuess[num]
    computerColor = colors[num]
    
    if playerGuess == computerColor:
      black_peg += 1
    elif playerGuess in colors:
      white_peg += 1
    else:
      grey_peg += 1
    
  return  black_peg,grey_peg,white_peg
    
    
  
  
