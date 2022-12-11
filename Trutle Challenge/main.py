from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
tim.color("cornflower blue")

for _ in range(4):
    tim.forward(90)
    tim.left(90)



screen = Screen()

screen.exitonclick()