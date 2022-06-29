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
score = Scoreboard()
screen.onkey(turtle.go, "w")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.generate_car()
    car.move_cars()
    for each_car in car.cars:
        if each_car.distance(turtle) < 20:
            score.game_over()
            game_is_on = False
    if turtle.finish_line():
        score.increase_lvl()
        turtle.go_to_start()
        car.lvl_up()


screen.exitonclick()




