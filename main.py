import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(2.5)




# Draw Walk
# colors = ["CornflowerBlue", "LawnGreen", "DarkOrchid", "teal", "navy", "red", "magenta", "blue", "orange", "purple"]
# directions = [0, 90, 180, 360]
# tim.pensize(15)


# for _ in range(200):
#     tim.color(color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# Draw hexagram

#
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

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


screen = t.Screen()
screen.exitonclick()
