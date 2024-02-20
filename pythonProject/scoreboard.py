from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "center"
level = 0


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=-210 , y=265)
        self.update_level()

    def update_level(self):
        global level
        level += 1
        self.clear()
        self.write(arg=f"Level: {level}", move=False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", move=False, align=ALIGN, font=FONT)


