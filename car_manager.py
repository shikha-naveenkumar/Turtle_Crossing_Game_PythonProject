import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]



class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 0.1

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            turtle = Turtle("square")
            turtle.shapesize(1, 2)
            turtle.penup()
            turtle.color(random.choice(COLORS))
            r_y = random.randint(-220, 220)
            turtle.goto(280, r_y)
            turtle.setheading(180)
            self.all_cars.append(turtle)



    def move(self):
        for i in self.all_cars:
            i.forward(self.STARTING_MOVE_DISTANCE)

    def car_refresh(self):
        for i in self.all_cars:
            self.STARTING_MOVE_DISTANCE = self.STARTING_MOVE_DISTANCE + self.MOVE_INCREMENT
            i.forward(self.STARTING_MOVE_DISTANCE)



