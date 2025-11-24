#File Purpose: Gives Game Rules and Takes User Inputs Intro
#Main Contributor to File: Sofia

file = open("gameRules.txt", "w")

Username = input("Enter your name to begin: ")

"\n\n"

# game rules
file.write(
    f"Welcome to Mastermind, {Username}!\n\n"
    "The game rules are simple: I will pick 3 colors and place them in a specific order.\n"
    "You will have 7 tries to figure out what I selected.\n\n"
    "Pegs on the side of the board will indicate if you have selected:\n"
    "the right color but wrong place,\n"
    "the right place but wrong color, or\n"
    "wrong color and wrong place.\n\n"
    "A black peg indicates a Code Peg of the right color and in the right position.\n"
    "A white peg indicates a Code Peg of the right color but in the wrong position.\n"
    "No peg means that color does not appear in the secret code.\n\n"
    "To begin, you will choose from 3 colors (Red, Blue, and Green)\n"
    "and type them in the order you think I put them in.\n"
    "You can enter your guess like this:'red', 'green', or 'blue'.\n")

file.close()

# Read
file = open("gameRules.txt", "r")

contents = file.read()
print(contents)

file.close()
