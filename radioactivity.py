import turtle
"""radioctivity"""
turtle.speed(200),
line_size = 14
turtle.pensize(2)
for i in range(1000):
    turtle.forward(line_size)
    turtle.left(121)
    turtle.forward(line_size)
    turtle.left(121)
    turtle.forward(line_size)
    line_size += 8
turtle.Screen().exitonclick()
