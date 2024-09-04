#doc. https://docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.listen()
screen.onkey()