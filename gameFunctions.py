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
      
  
    
    
  
  
