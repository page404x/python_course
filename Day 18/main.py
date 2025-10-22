from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.color("black")
canvas = Screen()


for i in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

canvas.exitonclick()


