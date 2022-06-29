from turtle import Turtle
import random
from random import randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        generate_chance = randint(1, 6)
        if generate_chance == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car_color = random.choice(COLORS)
            car.fillcolor(car_color)
            rand_pos_y = randint(-280, 280)
            car.goto(300, rand_pos_y)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def lvl_up(self):
        self.car_speed += MOVE_INCREMENT
