def random_Colors():
    """this function generates three random numbers and assigns them to a list, it then creates a new list of three colors corresponding to the numbers generated"""
    import random
    numbers = []
    for i in range(3):
        num = random.randint(1,3)
        numbers.append(num)
    colors = []
    for i in range(3):
        number = numbers[i]
        if number == 1:
            colors.append("red")
        elif number == 2:
            colors.append("blue")
        else:
            colors.append("green")
    return colors

def guess_checking(color_code):
    #takes the guesses from the user and puts them in a list
    order = ["first", "second", "third"]
    guesses = []
    for i in range(3):
        attempt = order[i]
        guess = input(f"Enter your guess for the {attempt} color: ")
        while guess != "red" and guess != "blue" and guess != "green":#error handling
            print("You must guess 'red', 'blue', or 'green'. Please guess again: ")
            guess = input(f"Enter your guess for the {attempt} color: ")
        guesses.append(guess)

    #creates copies of the lists to edit and adjust after checking colors
    guessable_colors = color_code.copy()
    guesses_made = guesses.copy()

    #checks if the guess is an exact match and assigns a black peg
    pegs = []
    for i in range(3):
        if guesses_made[i] == guessable_colors[i]:
            pegs.append("black")
            
            guessed = guesses_made[i]
            
            guessable_colors.remove(guessed)#if the color is in the code it removes it
            guessable_colors.insert(i, None)#so that a white peg won't be assigned
            
            guesses_made.remove(guessed)#keeps from checking a guess twice and
            guesses_made.insert(i, None)#falsely assigning a white peg
        else:
            pegs.append(None)

    #checks if the guess has the right color in the wrong place and assigns a white peg
    for i in range(3):
        if guesses_made[i] is not None:
            if guesses_made[i] in guessable_colors:
                pegs[i] = "white"
                guessable_colors[guessable_colors.index(guesses_made[i])] = None
                #also ensures that a color will not be used twice after a peg is colored
            else:
                pegs[i] = "blank"
    return pegs, guesses



