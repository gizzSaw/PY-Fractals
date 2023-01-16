import turtle
line_size = 2
for i in range(128):
    turtle.pensize(4)
    turtle.forward(line_size)
    turtle.left(120)
    turtle.forward(line_size)
    turtle.left(120)
    line_size += 12
turtle.Screen().exitonclick()
