# import colorgram
#
# # Extract 6 colors from an image.
# colors = colorgram.extract('colors.jpg', 30)
#
# rgb = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb.append(new_color)
#
# print(rgb)
import turtle as t
import random

turtle = t.Turtle()
turtle.shape("circle")
t.colormode(255)
turtle.speed("fastest")
turtle.penup()
turtle.hideturtle()
turtle.setheading(225)
turtle.forward(325)
turtle.setheading(0)
colors_list = [(237, 238, 242), (240, 238, 232), (241, 236, 239), (235, 241, 238), (198, 161, 95), (148, 85, 49), (127, 164, 194), (179, 157, 30), (63, 100, 134), (150, 60, 91), (195, 143, 159), (141, 24, 47), (60, 26, 39), (215, 207, 126), (20, 38, 72), (197, 100, 84), (61, 35, 26), (225, 169, 185), (63, 107, 68), (184, 91, 129), (35, 54, 109), (29, 56, 37), (42, 89, 29), (132, 174, 159), (99, 121, 168), (137, 37, 26), (90, 88, 10), (191, 185, 213), (67, 163, 101), (44, 152, 177)]

dots = 100

for dot_count in range(1, dots + 1):
    turtle.dot(20, random.choice(colors_list))
    turtle.forward(50)

    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)











screen = t.Screen()
screen.exitonclick()