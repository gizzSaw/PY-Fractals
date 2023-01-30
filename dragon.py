import turtle

# screen settings

WIDTH, HEIGTH = 1600, 900
screen = turtle.Screen()
screen.setup(WIDTH, HEIGTH)
screen.screensize(3 * WIDTH, 3 * HEIGTH)
screen.bgcolor('black')
screen.delay(0)
# turtle settings
leo = turtle.Turtle()
leo.pensize(3)
leo.speed(0)
leo.setpos(WIDTH // 4, -HEIGTH // 4 - 25)
leo.color('magenta')


gens = 14
axiom = 'XY'
chr_1, rule_1 = 'X', 'X+YF+'
chr_2, rule_2 = 'Y', '-FX-Y'
step = 4
angle = 90


def apply_rules(axiom):
    return ''.join([rule_1 if chr == chr_1 else
                    rule_2 if chr in chr_2 else chr for chr in axiom])


def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom


turtle.pencolor('white')
turtle.goto(-WIDTH // 2 + 60, HEIGTH // 2 - 100)
turtle.clear()
turtle.write(f'generation: {gens}', font={"Arial", 60, "normal"})

axiom = get_result(gens, axiom)
for chr in axiom:
    if chr == chr_1 or chr == chr_2:
        leo.forward(step)
    elif chr == '+':
        leo.right(angle)
    elif chr == '-':
        leo.left(angle)

screen.exitonclick()
