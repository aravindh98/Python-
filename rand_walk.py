import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

t = Turtle()
t.shape("turtle")
t.color("red")

def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray"]
angle =[0, 90, 180, 270]
# a= t.forward(random.randint(50, 75))
# b= t.right(random.choice(angle))
# c= t.left(random.choice(angle))
# d = t.back(random.randint(50,75))
# directions = [a, b, c]
#
# n = random.randint(10, 25)
# def rand_walk(n):
#     movement = random.choice(directions)

for _ in range(100):
    t.color(rand_color())
    t.setheading(random.choice(angle))
    t.width(15)
    t.forward(50)
    t.speed(56)
