"""
Turtle Race
"""
import turtle
import random
from PIL import Image


# ================= Instructions at the bottom of this file ===================


def screen_clicked(x, y):
    print('You pressed: x=' + str(x) + ', y=' + str(y))


def draw_background():
    filename = 'race_track.gif'

    try:
        image = Image.open(filename)
    except(FileNotFoundError, IOError):
        print("ERROR: Unable to find file " + filename)
        return

    window = turtle.Screen()
    window.setup(image.width + 100, image.height + 100, startx=0, starty=0)
    window.bgpic(filename)
    window.onclick(screen_clicked)


# ====================== DO NOT EDIT THE CODE ABOVE ===========================
y = 194
num = 0
if __name__ == '__main__':
    draw_background()

    # TODO 1) Create an empty list of turtles
    t_list = list()
    # TODO 2) Create a new turtle and set its shape to 'turtle

    # TODO 3) Set the turtle's speed to 3

    # TODO 4) Set the turtle's pen up

    # TODO 5) Use the turtle's goto() method to set its position on the left
    #  side of the screen

    # TODO 6) use a loop to repeat the previous instructions and create
    #  8 turtles lined up on the left side of the screen
    #  *HINT* click on the window to print the corresponding x, y location
    color_1 = 'red'
    color_2 = 1
    for i in range(8):
        if color_2 == 1:
            color_1 = 'red'
        if color_2 == 2:
            color_1 = 'orange'
        if color_2 == 3:
            color_1 = 'yellow'
        if color_2 == 4:
            color_1 = 'green'
        if color_2 == 5:
            color_1 = 'blue'
        if color_2 == 6:
            color_1 = 'purple'
        if color_2 == 7:
            color_1 = 'white'
        if color_2 == 8:
            color_1 = 'black'
        color_2 += 1
        t_list.append(turtle.Turtle())
        t_list[i].shape('turtle')
        t_list[i].speed(2)
        t_list[i].penup()
        t_list[i].goto(-416, y)
        t_list[i].color(color_1)
        y -= 56

    # TODO 7) Move each turtle forward a random distance between 1 and 20
    huh = 1
    completed = False
    x = None
    winner = None
    while not completed:
        for i in range(8):
            huh = random.randint(1, 99)
            print(huh)
            if 0 < huh < 5:
                t_list[i].forward(random.randint(-20, -20))
                huh = random.randint(1, 39)
                if huh == 5:
                    t_list[i].forward(random.randint(100, 1000))
            if huh > 5:
                t_list[i].forward(random.randint(0, 3))
            x = t_list[i].xcor()
            if x > 349:
                completed = True
                winner = i
                if winner == 0:
                    winner = 'Red'
                if winner == 1:
                    winner = 'Orange'
                if winner == 2:
                    winner = 'Yellow'
                if winner == 3:
                    winner = 'Green'
                if winner == 4:
                    winner = 'Blue'
                if winner == 5:
                    winner = 'Purple'
                if winner == 6:
                    winner = 'White'
                if winner == 7:
                    winner = 'Black'
    for i in range(10):
        print(winner, "won!")
    if winner == 'Red':
        t_list[0].goto(0, 0)
        t_list[0].shapesize(20)
    if winner == 'Orange':
        t_list[1].goto(0, 0)
        t_list[1].shapesize(20)
        t_list[1].right(1080)
    if winner == 'Yellow':
        t_list[2].goto(0, 0)
        t_list[2].shapesize(20)
        t_list[2].right(1080)
    if winner == 'Green':
        t_list[3].goto(0, 0)
        t_list[3].shapesize(20)
        t_list[3].right(1080)
    if winner == 'Blue':
        t_list[4].goto(0, 0)
        t_list[4].shapesize(20)
        t_list[4].right(1080)
    if winner == 'Purple':
        t_list[5].goto(0, 0)
        t_list[5].shapesize(20)
        t_list[5].right(1080)
    if winner == 'White':
        t_list[6].goto(0, 0)
        t_list[6].shapesize(20)
        t_list[6].right(1080)
    if winner == 'Black':
        t_list[7].goto(0, 0)
        t_list[7].shapesize(20)
        t_list[7].right(1080)
    # TODO 8) Create a loop to keep moving each turtle until a turtle
    #  crosses the finish line
    #  *HINT* click on the window to print the corresponding x, y location

    # TODO 9) When a turtle crosses the finish line, stop the race and
    #  indicate which turtle won the race.

    # EXTRA: Create different colors for each turtle and code a special
    # dance for the winning turtle!
    turtle.done()
