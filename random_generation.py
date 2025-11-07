def random_Colors():
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



