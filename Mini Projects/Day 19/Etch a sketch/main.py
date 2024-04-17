from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_clockwise():
    tim.right(10)

def move_counterclock():
    tim.left(10)

def clear():
    tim.reset()


screen.listen() # Set focus on TurtleScreen (in order to collect key-events). Dummy arguments are provided in order to be
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counterclock)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()