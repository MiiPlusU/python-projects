import colorgram
import turtle as turtle_module
import random

# colors = colorgram.extract('image.jpg', 30)
#
# color_list = []
#
# for item in colors:
#
#     color = item.rgb
#     color_list.append(tuple(color))
turtle_module.colormode(255)
color_list = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]
tim = turtle_module.Turtle()

for _ in range(10):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

screen = turtle_module.Screen()
screen.exitonclick()