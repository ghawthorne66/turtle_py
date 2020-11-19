
from turtle import Turtle, Screen
import random


tim = Turtle()


tim.shape("turtle")
tim.color("blue")

#Draw hexagram

colors = ["teal", "navy", "red", "magenta", "blue", "orange", "purple", "green"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 10):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

# draw_shapes(5)

# Draw Square

# def square():
#     on = True
#     while on:
#         for i in range(8):
#             tim.forward(30)
#             tim.up()
#             tim.forward(10)
#             tim.down()
#
#         tim.right(90)
#
#
# square()





# timmy_the_turtle.backward(200)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)







screen = Screen()
screen.exitonclick()

