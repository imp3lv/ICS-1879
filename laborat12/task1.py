import turtle

def run_commands(commands):
    t = turtle.Turtle()
    for cmd in commands.upper():
        if cmd == 'F':
            t.forward(50)
        elif cmd == 'L':
            t.right(90)
        elif cmd == 'R':
            t.left(90)
        elif cmd == 'U':
            t.penup()
        elif cmd == 'D':
            t.pendown()
    turtle.done()

commands = input("Введіть команди (F, L, R, U, D): ")
run_commands(commands)
