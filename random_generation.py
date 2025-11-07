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
            colors.append("Red")
        elif number == 2:
            colors.append("Blue")
        else:
            colors.append("Green")
    return colors




