import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)
car = CarManager()
turtle = Player()
screen.listen()

screen.onkey(turtle.go, "w")


game_is_on = True
turtle.go_to_start()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.generate_car()
    car.move_cars()



