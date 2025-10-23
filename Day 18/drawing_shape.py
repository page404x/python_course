from turtle import Turtle, Screen

tim = Turtle()
canvas = Screen()
pen_color = ["red", "green", "yellow", "blue", "orange", "light gray", "gray", "black"]
def build_shape(sisi):
    sud = 360/sisi
    for i in range(sisi):
        tim.forward(100)
        tim.right(sud)

color_index = 0

for i in range(3, 11):
    tim.pencolor(pen_color[color_index])
    build_shape(i)
    color_index +=1
canvas.exitonclick()