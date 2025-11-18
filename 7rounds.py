import guess_checker_function as gcf
import random_generation as gen
import create_board as cb
import gameRules as gr



color_code = gen.()

for i in range(7):
    print(f"Round {i+1}")
    result = gcf.guess_checking(color_code)
    pegs = result[0]
    guesses = result[1]
    if "white" not in pegs and "blank" not in pegs:
        print("Congratulations!!!\n You solved the Secret Code!")
        break
    elif "white" in pegs or "blank" in pegs:
        print("Looks like you're still missing some of the code! \n Try again!")

