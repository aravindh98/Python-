import random
import turtle
from turtle import Turtle

# import colorgram
#
# colors = colorgram.extract('image.jpg', 25)
# color_list =[]
# for n in range(0, 25):
#     color = colors[n]
#     rgb = color.rgb
#     r = rgb[0]
#     g = rgb[1]
#     b = rgb[2]
#     ori_color = (r, g, b)
#     color_list.append(ori_color)
#
# print(color_list)
turtle.colormode(255)
t1 = Turtle()
t1.penup()
t1.speed("fastest")
t1.hideturtle()
t1.setheading(225)
t1.forward(300)
t1.setheading(0)
list_colors = [(124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]
# for color in list_colors:
#     t1.speed("slowest")
#     t1.penup()
#     t1.forward(50)
#     t1.pendown()
#     t1.dot(20, color)
num_of_dots = 101

for dot_count in range (1, num_of_dots):
    t1.dot(20, random.choice(list_colors))
    t1.forward(50)

    if dot_count % 10 == 0:
        t1.setheading(90)
        t1.forward(50)
        t1.setheading(180)
        t1.forward(500)
        t1.setheading(0)

screen = turtle.Screen()
screen.exitonclick()

