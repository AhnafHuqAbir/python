import turtle

def draw_circle(x, y, r, color="black", fill=True):
    turtle.penup()
    turtle.goto(x, y - r)
    turtle.pendown()
    turtle.color(color)
    if fill:
        turtle.begin_fill()
    turtle.circle(r)
    if fill:
        turtle.end_fill()

def draw_hat():
    # Draw the brim
    turtle.penup()
    turtle.goto(-70, 100)
    turtle.pendown()
    turtle.color("black")
    turtle.width(20)
    turtle.forward(140)
    turtle.width(1)
    # Draw the top
    draw_circle(0, 160, 60, "black", fill=True)

def draw_face():
    draw_circle(0, 0, 70, "peachpuff", fill=True) # Face

def draw_eyes():
    # Left eye
    draw_circle(-30, 30, 10, "white", fill=True)
    draw_circle(-30, 30, 3, "black", fill=True)
    # Right eye
    draw_circle(30, 30, 10, "white", fill=True)
    draw_circle(30, 30, 3, "black", fill=True)

def draw_eyebrows():
    # Left eyebrow
    turtle.penup()
    turtle.goto(-45, 55)
    turtle.setheading(20)
    turtle.pendown()
    turtle.width(5)
    turtle.forward(30)
    turtle.width(1)
    # Right eyebrow
    turtle.penup()
    turtle.goto(15, 60)
    turtle.setheading(160)
    turtle.pendown()
    turtle.width(5)
    turtle.forward(30)
    turtle.width(1)

def draw_mustache():
    # Left half
    turtle.penup()
    turtle.goto(-18, -10)
    turtle.setheading(210)
    turtle.pendown()
    turtle.width(8)
    turtle.circle(15, 60)
    # Right half
    turtle.penup()
    turtle.goto(18, -10)
    turtle.setheading(-30)
    turtle.pendown()
    turtle.circle(-15, 60)
    turtle.width(1)

def draw_mouth():
    turtle.penup()
    turtle.goto(-20, -40)
    turtle.setheading(-60)
    turtle.pendown()
    turtle.width(3)
    turtle.circle(20, 120)
    turtle.width(1)

def draw():
    turtle.speed(1)
    turtle.hideturtle()
    turtle.bgcolor("white")
    draw_hat()
    draw_face()
    draw_eyebrows()
    draw_eyes()
    draw_mustache()
    draw_mouth()
    turtle.done()

if __name__ == "__main__":
    draw()