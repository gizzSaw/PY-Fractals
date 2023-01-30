import turtle
line_size = 2
turtle.speed(200),
for i in range(512):
    turtle.pensize(4)
    turtle.forward(line_size)
    turtle.left(120)
    turtle.forward(line_size)
    turtle.left(120)
    line_size += 12
turtle.Screen().exitonclick()
