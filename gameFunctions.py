#Game Functions

def play_again():
"""This function asks the player if they would like to begin a new game round"""
  while True:
    again = input("Would you like to play again? (y/n): ").lower
    if again == "y":
        return True
    if again == "n":
        return False
    else:
        print("Invalid input. Goodbye!")
        break

import random_Colors() as rc
import create_board() as cb
def guess_check():
  colors = rc.colors
  guess1 = cb.Circle1
  guess2 = cb.Circle2
  guess3 = cb.Circle3
  while guess1 != colors[0]:
    return False
    if true:
      
  while guess2 != colors[1]:
    return False
  while guess3 != colors[2]:
    return False
  
    
    
  
  
