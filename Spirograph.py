import turtle,random
from turtle import Turtle

t1 = Turtle()
turtle.colormode(255)
def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color



# My Code
# for _ in range(40):
#     t1.speed("fastest")
#     t1.color(rand_color())
#     t1.circle(100)
#     t1.speed("fastest")
#     # t1.left(10)
# current_heading = t1.heading()
# t1.setheading(current_heading + 10)
def draw_spiral(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t1.speed("fastest")
        t1.color(rand_color())
        t1.circle(100)
        current_heading = t1.heading()
        t1.setheading(current_heading + size_of_gap)

draw_spiral(5)