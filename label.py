from turtle import Turtle

class Label(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('black')

    def move(self,x,y):
        self.goto(x,y)



