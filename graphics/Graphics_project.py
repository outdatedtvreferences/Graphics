import turtle

import math

screen = turtle.Screen()

screen.bgcolor("blue")

screen.title("Frosty the snowman!")



frosty = turtle.Turtle()

frosty.speed(0)

frosty.color("black")

frosty.fillcolor("white")

frosty.pensize(3)

frosty.hideturtle()

def face (x, y):

    frosty.up()

    frosty.goto(x + 10,y)

    frosty.dot()

    frosty.goto(x - 10,y)

    frosty.dot()

    frosty.goto(x,y -10)

    frosty.dot()

    frosty.goto(x -15,y -25)

    frosty.down()

    frosty.forward(30)

    frosty.up()

    def arm(x,y,length,heading):

        frosty.up()

        frosty.goto(x,y)

        frosty.setheading(heading)

        frosty.down()

        frosty.forward(length)

        frosty.setheading(heading + 20)

        frosty.forward(20)

        frosty.up()

        frosty.back(20)

        frosty.down()

        frosty.setheading(heading - 20)

        frosty.forward(20)

        frosty.up()

        frosty.home()



        def circle(radius,y):

            frosty.up()

            frosty.sety(y)

            arc_length = 1 * (math.pi/180) * radius



            frosty.down()



            frosty.begin_fill()



            for i in range (360):

                frosty.forward(arc_length)

            frosty.up()

            frosty.end_fill()





            circle(40,20)

            circle(70,-120)

            circle(100,-320)

            arm(70,-50,50,20)

            arm(-70,-50,50,160)

            face(0,70)



            screen.exitonclick()

        

    

    
