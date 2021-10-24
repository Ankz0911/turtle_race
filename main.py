from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)

colors = ["red", "green", 'orange', 'purple', 'blue', 'black']
y_positions = [150, 100, 50, 0, -50, -100]
turtles = []
is_game_on = False

for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(-230, y_positions[i])
    turtles.append(tim)

user_bet = screen.textinput("Place a bet", "Which color turtle will win ? ")
if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in turtles:
        x_coordinate = turtle.xcor()

        if x_coordinate >= 230:
            if user_bet == turtle.pencolor():
                print(f'You won , The winning turtle is {turtle.pencolor()}.')
                is_game_on = False
            else:
                print(f'You lost , The winning turtle is {turtle.pencolor()}.')
                is_game_on = False
        else:
            turtle.forward(random.randint(0, 10))

screen.exitonclick()
