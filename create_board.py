def create_board():
    import turtle
    t = turtle.Turtle(shape = "turtle")
    t.color("black")
    t.pensize(5)
    t.speed(100)
    t.ht()

    y_coord = 300
    for i in range(7):
        x_coord = -100
        for i in range(3):
            t.up()
            t.goto(x_coord,y_coord)
            t.down()
            t.circle(25)
            x_coord += 100
        y_coord -= 100

    ycoord = 315
    for i in range(7):
        xcoord = 175
        for i in range(3):
            t.up()
            t.goto(xcoord,ycoord)
            t.down()
            t.circle(10)
            xcoord += 50
        ycoord -= 100
    return t
    
def fillColors(t):
    import turtle
    t = turtle.Turtle(shape = "turtle")
    t.ht()
    
    y_coord = 300  # Start at top row
    print("Enter your guess left to right. Options: red, blue, or green")

    for round_num in range(1, 8): 

        Circle1 = input(f"Round {round_num} guess 1/3: ").lower()
        Circle2 = input(f"Round {round_num} guess 2/3: ").lower()
        Circle3 = input(f"Round {round_num} guess 3/3: ").lower()

        x_coord = -100  # start at left circle

        # Fill the row with colors the user inputs
        for color in [Circle1, Circle2, Circle3]:
            t.up()
            t.goto(x_coord, y_coord)
            t.down()
            t.fillcolor(color)
            t.begin_fill()
            t.circle(25)
            t.end_fill()
            x_coord += 100
           
        y_coord -= 100  # move to next row

    turtle.done()
