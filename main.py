from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=600, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
vertical = -120
all_turtles = []
for turtle_index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x=-230, y=vertical)
    vertical += 50
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 250:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won")
            else:
                print(f"You've lost. The winning color is {winning_color}.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

#
#
# def move_forwards():
#     tim.fd(10)
#
#
# def move_backwards():
#     tim.bk(10)
#
#
# def counter_clockwise():
#     tim.lt(10)
#
#
# def clockwise():
#     tim.rt(10)
#
#
# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=counter_clockwise)
# screen.onkey(key="d", fun=clockwise)
# screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()