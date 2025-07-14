import turtle

screeen = turtle.Screen()
screeen.bgcolor("lightgreen")
screeen.title("Parten Deaw")
screeen.setup(600,600)

t = turtle.Turtle()
t.pensize(2)
t.color("green")
t.shape("turtle")
t.speed(2)
t.fillcolor("green")

t.begin_fill()
t.forward(300)
t.left(90)
t.forward(200)
t.left(90)
t.forward(300)
t.left(90)
t.forward(200)
t.end_fill()

t.hideturtle()

turtle.done()