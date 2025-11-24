
#Project Title: Mastermind
#Course: CS118 Fundamental of Programming
#Instructor: Dr. O
#Submission Date: 2025-11-25
#Project Type: Group
#Group Members:
# - Danica Quinn
# - Sofia Bustamante-Guzman
# - Nyx Silva
#File Purpose: Main Program File

import turtle as t
import gameRules as G
import gameFunctions as F
import guess_checker_function as gcf
import create_board as cb


while True:#Loop to enable play again functionality
#Present Game Rules
    file = open("gameRules.txt","r")
    file.read()
    file.close()

    game_board = cb.create_board()

    color_code = gcf.random_Colors()
#Starts Loop to Play Game
    for round_num in range(1,8):
        print(f"Round {round_num}")
        result = gcf.guess_checking(color_code)
        pegs = result[0]
        guesses = result[1]
        gameColors = cb.fillColors(t,guesses,round_num)
        pegColors = cb.fillPegs(t,pegs,round_num)
    
        if "grey" not in pegs and "white" not in pegs:
            print("Congratulations!!!\n You solved the Secret Code!")
            break
        elif "grey" in pegs or "white" in pegs:
            print("Looks like you're still missing some of the code! \n Try again!")
    print("Game Over!")
    
    if not F.play_again():
        print("Thanks for playing!")
        break
    else:
        t.clearscreen()




    




