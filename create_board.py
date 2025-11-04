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
