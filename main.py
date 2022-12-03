import colorgram as cg
import turtle as tur
from random import randint

x_size = 1441
y_size = 761
n_bols = 22
colors = cg.extract('image.jpg', 20)
my_screen = tur.Screen()
my_screen.setup(x_size, y_size, 0, 0)
tur.colormode(255)
my_turtle = tur.Turtle()
my_turtle.speed(0)
my_turtle.pensize(25)
my_turtle.penup()
my_turtle.setpos(-695.5, -340)

number = 0
for _ in range(12):
    for c in range(n_bols - 1):
        my_turtle.dot(32.75, colors[randint(0, 19)].rgb)
        my_turtle.forward(65.5)
    my_turtle.dot(32.75, colors[randint(0, 9)].rgb)
    if number == 0:
        my_turtle.left(90)
        my_turtle.forward(60.5)
        my_turtle.left(90)
        number = 1
    else:
        my_turtle.right(90)
        my_turtle.forward(65.5)
        my_turtle.right(90)
        number = 0

my_screen.exitonclick()
