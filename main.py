import time
from turtle import Screen
from player import Player, FINISH_LINE_Y, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


screen.listen()
player = Player()
car = CarManager()
scoreboard = Scoreboard()
screen.onkey(fun=player.move_forward, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.car_move()

    for any_car in car.all_cars:
        if player.distance(any_car) < 15:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() == FINISH_LINE_Y:
        player.setpos(STARTING_POSITION)
        scoreboard.level_up()
        car.speed += 1


screen.exitonclick()