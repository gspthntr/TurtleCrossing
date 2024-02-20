import time
from turtle import Screen
from player import Player
from car_manager import Cars
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()

screen.onkeypress(fun=player.mv_forward, key="w")
screen.listen()


counter = 0
game_is_on = True
cars = []

while game_is_on:
    time.sleep(0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
    screen.update()
    counter += 1
    if counter % 25 == 0:
        c = Cars()
        cars.append(c)
        counter = 0
    for car in cars:
        car.drive()
        if car.xcor() < -330:
            car.goto(x=1000, y=1000)
            del cars[cars.index(car)]
        if player.distance(car) < 22:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > 280:
        car.increase_car_speed()
        scoreboard.update_level()
        player.goto(x=0, y=-280)


screen.exitonclick()
