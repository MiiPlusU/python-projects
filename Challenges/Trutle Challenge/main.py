from turtle import Turtle, Screen
import random

tim = Turtle()

tim.shape("turtle")
tim.color("purple")

num_of_sides = 3

screen = Screen()
screen.colormode(255)


def random_color():

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

angle = 20

tim.speed("fastest")

for _ in range(300):

    tim.pencolor(random_color())
    tim.settiltangle(angle)
    tim.setheading(angle)
    tim.circle(100)
    angle+=10

    if angle == 360:
        break


screen.exitonclick()