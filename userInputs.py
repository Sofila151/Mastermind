#User Inputs For Guesses
import turtle as t
import gameRules as G
import gameFunctions as F
import random_generation_function as R
import guess_checker_function as C
#Present Game Rules
file = open("gameRules.txt","r")

file.read()

file.close()

#Select Colors
randomColors = R.random_Colors()

#import game board to play
import create_board as B
gameBoard = B.create_board()

for round_num in range(7):
    user_guess = F.userGuesses()
    gameColors = B.fillColors(t,user_guess,round_num)
    checkGuess = C.guess_checking(colorCode) # Code they are guessing
    
    
    playNew = F.play_again()



# Next Steps:
# Then, implement UI to fill in

# Attatch Score Board File

    
#also rename this file to "Main"



    




