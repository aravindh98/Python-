from turtle import Turtle,Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
user_ans = screen.textinput(title="Make your Bet", prompt="Which turtle will win the race? Enter the color:")
print(user_ans)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]



y_pos =[-70, -40, -10, 20, 50, 80]
is_game_on = False

turtle_list = []

for i in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_pos[i])
    turtle_list.append(new_turtle)


if user_ans:
   is_game_on = True

while is_game_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_ans:
                print(f" You won!! The {winning_color} turtle is winning!!")
            else:
                print(f" You lose!! The {winning_color} turtle is winning!!")



        turt_dist = random.randint(0, 10)
        turtle.forward(turt_dist)








screen.exitonclick()
