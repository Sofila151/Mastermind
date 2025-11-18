import guess_checker_function as gcf
import random_generation_function as gen
import create_board as cb
import gameRules as gr
import turtle as t

file = open("gameRules.txt","r")

file.read()

file.close()

game_board = cb.create_board()

color_code = gen.random_Colors()

for round_num in range(1,8):
    print(f"Round {round_num}")
    result = gcf.guess_checking(color_code)
    pegs = result[0]
    guesses = result[1]
    for i in range(3):
        gameColors = cb.fillColors(t,guesses,round_num)
    if "white" not in pegs and "blank" not in pegs:
        print("Congratulations!!!\n You solved the Secret Code!")
        break
    elif "white" in pegs or "blank" in pegs:
        print("Looks like you're still missing some of the code! \n Try again!")




