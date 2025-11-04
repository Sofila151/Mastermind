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
def guess_checker():
"""This function check the players inputs against the computer selection"""
    for i in range(user_guess):
        if user_guess[i] not in colors:
            return False
        return True

def score(colors, guess):
"""This function score the players game"""
  right = 0
  rightW = 0 
  for i in range(0, len(colors)):
    if guess[i] == colors[i]:
      right += 1
    if guess[i] in code and guess[i] != code[i]:
      rightW += 1
  return tuple([right, rightW])

def main():
"""This function allows the player to make a guess"""
    colors = ["r","g","b","red","green","blue"] 
    attempts = 0
    while True:
        user_guess = input("Enter your guess: ")

        if user_guess == colors:
            print("You got it in one try, congratulations, you're a Mastermind!")
            play_again()
        if guess_checker(user_guess, colors) == True:
            print(score(colors, user_guess))
            attempts += 1
