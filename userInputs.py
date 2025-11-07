#User Inputs For Guesses
import turtle as t
import gameRules as G
import gameFunctions as F
import random_generation as R

#Present Game Rules
file = open("gameRules.txt","r")

file.read()

file.close()

#Select Colors
randomColors = R.random_Colors()

#import game board to play
import create_board as B

gameBoard = B.create_board()
gameColors = B.fillColors(t)


# Next Steps:
#Asks the player if they would like to play a new round
playNew = F.play_again()

# checkGuess = guess_checker()  So we can check if the users answer is correct
# Then, implement UI 

# Attatch Score Board File


    
#also rename this file to "Main"



    




