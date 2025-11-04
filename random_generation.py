import random

def number_generator():
    numbers = []
    for i in range(3):
        num = random.randint(1,3)
        numbers.append(num)
    return numbers

numbers = number_generator()
print(numbers)

def assign_colors(numbers):
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

colors = assign_colors(numbers)
print(colors)
