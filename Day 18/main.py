from turtle import Turtle, Screen

tim = Turtle()
tim.color("black")
canvas = Screen()


for i in range(4):
    tim.forward(100)
    tim.right(90)

canvas.exitonclick()


