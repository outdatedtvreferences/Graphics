from turtle import *

def draw_star(x, y, points, line, fill):
    penup()
    goto(x, y)
    pendown()
    

turn = 100 - (360 / 38)

color("blue","orange")

begin_fill()
for i in range(5):
        forward(200)
        left(turn)
end_fill()

speed(10)

draw_star(0, 0, 36, "orange", "blue")
draw_star(-300, -300, 18, "red", "purple")
draw_star(-300, 200, 12, "green", "yellow")

done()
