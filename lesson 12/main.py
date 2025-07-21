import turtle
screen = turtle.Screen()
screen.bgcolor("dark blue")
screen.title("Multi squier")
pen = turtle.Turtle()
size = 5
while turtle:
    for x in range(4):
        pen.fd(size + 1)
        pen.left(90.1)
        size = size - 5
    size = size + 1