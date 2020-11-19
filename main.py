
from turtle import Turtle, Screen


tim = Turtle()


tim.shape("turtle")
tim.color("blue")

# for _ in range(12):
#     tim.forward(100)
#     tim.right(90)


def square():
    on = True
    while on:
        for i in range(8):
            tim.forward(30)
            tim.up()
            tim.forward(10)
            tim.down()

        tim.right(90)


square()




# timmy_the_turtle.backward(200)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)







screen = Screen()
screen.exitonclick()

