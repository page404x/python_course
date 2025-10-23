from turtle import Turtle, Screen

pen = Turtle()
pen.color("black")
canvas = Screen()

for i in range(10):
    pen.pendown()
    pen.forward(10)
    pen.penup()
    pen.forward(10)


canvas.exitonclick()
