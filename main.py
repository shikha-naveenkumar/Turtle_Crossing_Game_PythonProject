from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()
s = Turtle()
s.hideturtle()

screen.listen()
screen.onkey(player.go_up, "Up")

s.penup()
s.goto(-280,250)
s.write(f"Level: {score.level}", "center", font=("Ariel", 20, "bold"))

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    for i in car.all_cars:
        if i.distance(player) < 20:
            game_is_on = False
            tim = Turtle()
            tim.penup()
            tim.goto(-60,0)
            tim.write(f"Game Over!!", "center", font=("Ariel", 20, "bold"))

    if player.ycor() == 280:
        s.clear()
        player.refresh()
        car.car_refresh()
        score.update()
        s.penup()
        s.goto(-280,250)
        s.write(f"Level: {score.level}", "center", font=("Ariel", 20, "bold"))








screen.exitonclick()

