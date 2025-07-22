import turtle
screen = turtle.Screen()
screen.bgcolor("dark blue")
screen.title("Multi squier")
screen.setup(800,800)
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(7)
size = 5
while turtle:
    for x in range(4):
        pen.fd(size + 1)
        pen.left(270)
        size = size - 5
    size = size + 1
