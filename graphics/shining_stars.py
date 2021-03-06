from turtle import *

def draw_star(x, y, points, line, fill):
    penup()
    goto(x, y)
    pandown()

turn = 100 - (360 / 38)

color(line,fill)

begin_fill()
for i in range(points):
        forward(200)
        left(turn)
end_fill()

speed(10)

    draw_star(0, 0, 36, "orange", "blue")
draw_star(-300, -300, 18, "red", "purple")
draw_star(-300, 200, 12, "green", "yellow")

done()
