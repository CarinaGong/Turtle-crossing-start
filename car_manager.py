from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.speed = 0

    def create_car(self):
        random_choice = randint(0, 6)
        if random_choice == 1:
            new_car = Turtle("square")
            new_car.setheading(180)
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.setx(280)
            new_car.sety(randint(-250, 250))
            self.all_cars.append(new_car)

    def car_move(self):
        for new_car in self.all_cars:
            new_car.forward(STARTING_MOVE_DISTANCE + self.speed * MOVE_INCREMENT)
