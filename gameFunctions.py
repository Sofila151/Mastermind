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

def guess_check():
  
