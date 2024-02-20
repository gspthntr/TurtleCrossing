from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 1


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(COLORS[randint(0, 5)])
        self.penup()
        self.goto(x=315, y=randint(-240, 240))
        self.left(180)

    def drive(self):
        self.forward(STARTING_MOVE_DISTANCE)

    def increase_car_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT

