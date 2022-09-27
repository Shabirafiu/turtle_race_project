import random
import turtle
from turtle import Turtle, Screen


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="place your Bet asap!",prompt="pick your best Turtle? Enter a color: ")
colors = ["thistle","red","blue","green","purple"]
y_positions = [-70,-40,-10,20,50,80]
all_tutles = []

for turtle_index in range(0,5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    #tim.shape("turtle ")
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_tutles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_tutles:
        if turtle.xcor() >230:
            is_race_on = False
            winning_colors = turtle.pencolor()
            if winning_colors == user_bet:
                print(f"You've won {winning_colors} turtle is winner")

            else:
                print(f"You've lost {winning_colors} turtle is winner")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()




















#def move_forward():
#    tim.forward(10)
#
#def move_backwards():
#    tim.backward(10)
#
#def turn_left():
#    new_heading = tim.heading() + 10
#    tim.setheading(new_heading)
#
#def turn_right():
#    new_heading = tim.heading() - 10
#    tim.setheading(new_heading)
#
#def clear():
#    tim.clear()
#    tim.home()
#
#
#screen.listen()
#screen.onkey(move_forward, "w")
#screen.onkey(move_backwards, "s")
#screen.onkey(turn_left, "a")
#screen.onkey(turn_right, "d")
#screen.onkey(clear,"c")
#screen.exitonclick()