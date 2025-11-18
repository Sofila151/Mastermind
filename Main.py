#User Inputs For Guesses
import turtle as t
import gameRules as G
import gameFunctions as F
import guess_checker_function as gcf
import create_board as cb


#Present Game Rules
file = open("gameRules.txt","r")

file.read()

file.close()

game_board = cb.create_board()

color_code = gcf.random_Colors()

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

playNew = F.play_again()



# Next Steps:
# Then, implement UI to fill in peg call list from guess checkers 

# Attatch Score Board File

    
#also rename this file to "Main"



    




