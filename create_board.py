def create_board():
    """This function creates the game board base"""
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
    
def fillColors(t,userGuesses,round_num):
    """This function collects the users input and then fills in the circles with the corresponding colors"""
    y_coord = 300 - (round_num * 100)
    x_coord = -100

    for colors in userGuesses:
            t.up()
            t.goto(x_coord, y_coord)
            t.down()
            t.fillcolor(colors)
            t.begin_fill()
            t.circle(25)
            t.end_fill()
            x_coord += 100
    return t

def fillColors(t,userGuesses,round_num):
    """This function collects the users input and then fills in the circles with the corresponding colors"""
    y_coord = 315 - (round_num * 100)
    x_coord = 175

    for colors in userGuesses:
            t.up()
            t.goto(x_coord, y_coord)
            t.down()
            t.fillcolor(colors)
            t.begin_fill()
            t.circle(25)
            t.end_fill()
            x_coord += 100
            
    return t
        
        


# Call list from guess checker 
