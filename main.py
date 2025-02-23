import turtle
import pandas
from label import Label

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

point = Label()
data = pandas.read_csv("50_states.csv")
states = data.state

guessed_states = []

while len(guessed_states) < 50:
    answer_states = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                     prompt="What's another state's name").title()
    for i in states:
        if answer_states in guessed_states:
            pass
        elif answer_states == i:
            guessed_states.append(answer_states)
            axis = data[data.state == answer_states]
            x = int(axis.x.iloc[0])
            y = int(axis.y.iloc[0])
            point.move(x, y)
            point.write(answer_states)

screen.exitonclick()