import turtle
import random

def main():
    tt1 = turtle.Turtle()
    tt2 = turtle.Turtle()
    tt3 = turtle.Turtle()
    s = turtle.Screen()         # Save the screen (window) as s
    window = turtle.Screen()

    colors = ("red", "orange", "blue", "green", "white", "yellow", "indigo", "pink")

    s.setup(1200,900)           # Set the window size to 1200 width, 900 height
    turtle.bgcolor("black")
    # Speed setting
    turtle.speed(100000)

    tt1.hideturtle()
    tt2.hideturtle()
    tt3.hideturtle()

    draw(-300, -300, 'green', tt1)
    draw(0, 100, 'yellow', tt1)
    draw(350, -200, 'green', tt1)
    draw_stars(50, tt2, colors)
    drawRyan(tt3, window)

    window.exitonclick()

def draw_stars(r, t2, c):
    for x in range(r):
        t2.up()
        t2.goto(random.randint(-500, 500), random.randint(200, 500))
        t2.down()
        # Draw a star
        t2.color(random.choice(c))
        t2.begin_fill()
        star_size = random.randint(10, 30)
        
        for i in range(5):
            t2.forward(star_size)
            t2.left(144)
        t2.end_fill()
        
def drawTree(branch, t1, leaf):
    t1.color('brown')
    t1.width(8)

    if branch < 10:
        return
    else:
        t1.forward(branch)

        green_shape = random.uniform(0.3, 0.9)
        if leaf == 'green':
            t1.color(0.0, green_shape, 0.0) 
        else:
            t1.color(green_shape, green_shape, 0.0)

        t1.begin_fill()
        t1.circle(10)
        t1.end_fill()

        t1.left(20)
        drawTree(branch-15, t1, leaf)
        t1.right(40)
        drawTree(branch-15, t1, leaf)
        t1.left(20)
        t1.backward(branch)

def draw(x, y, leaf, t1):
    t1.setheading(90)
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    drawTree(90, t1, leaf)

def drawRyan(t3, win):
    t3.pensize(5)                        # Set pen size to 5 (thicker line)
    t3.color("black", "#f0a53a")         # Pen color: black, fill color: Ryan-like orange

    # Draw Ryan's body
    t3.penup()                           # Pen up to move without drawing
    t3.goto(-190, -80)                   # Move to left shoulder
    t3.pendown()                         # Pen down to start drawing
    t3.begin_fill()                      # Start filling shape (until end_fill)
    t3.setheading(220)                   # Change drawing direction to 220 degrees
    t3.circle(80, 100)                   # Draw left arm as arc (100 degrees)
    t3.setheading(270)                   # Change direction downward (270 degrees)
    t3.forward(100)                      # Draw left leg (move 100 units)
    t3.circle(35, 180)                   # Draw left foot as a half circle (180 degrees)
    t3.forward(20)
    t3.right(90)
    t3.forward(40)
    t3.right(90)
    t3.forward(20)
    t3.circle(35, 180)                   # Draw right foot as a half circle
    t3.forward(100)
    t3.setheading(40)
    t3.circle(80, 100)                   # Draw right arm as arc
    t3.goto(-190, -80)                   # Return to start point (left shoulder)
    t3.end_fill()                        # Fill the shape's area
    
    # Separate arms from body with lines
    # Left arm separator
    t3.penup()
    t3.goto(-190, -130)
    t3.pendown()
    t3.goto(-190, -200)
    # Right arm separator
    t3.penup()
    t3.goto(-10, -130)
    t3.pendown()
    t3.goto(-10, -200)

    # Draw chest pattern
    t3.color("white", "white")           # Both pen and fill color: white
    t3.penup()
    t3.goto(-60, -140)
    t3.pendown()
    t3.begin_fill()
    t3.goto(-80, -160)
    t3.goto(-100, -140)
    t3.goto(-120, -160)
    t3.goto(-140, -140)
    t3.setheading(240)
    t3.circle(47, 240)                   # Draw arc, 240 degrees
    t3.end_fill()

    # Draw ears
    t3.color("black", "#f0a53a")         # Pen color: black, fill color: Ryan-like orange
    # Left ear
    t3.penup()
    t3.goto(-170, 110)
    t3.pendown()
    t3.begin_fill()
    t3.setheading(120)
    t3.circle(30, 210)                   # Arc, 210 degrees
    t3.end_fill()
    # Right ear
    t3.penup()
    t3.goto(-30, 110)
    t3.pendown()
    t3.begin_fill()
    t3.setheading(60)
    t3.circle(-30, 210)                  # Negative radius for opposite arc direction
    t3.end_fill()

    # Draw head
    t3.penup()
    t3.goto(-100, 130)
    t3.pendown()
    t3.begin_fill()
    t3.setheading(180)
    t3.circle(130)                       # Full circle for the face
    t3.end_fill()

    t3.pensize(10)
    # Left eyebrow
    t3.penup()
    t3.goto(-180, 30)
    t3.pendown()
    t3.goto(-130, 30)
    # Right eyebrow
    t3.penup()
    t3.goto(-20, 30)
    t3.pendown()
    t3.goto(-70, 30)

    # Left eye
    t3.penup()
    t3.goto(-155, 10)
    t3.pendown()
    t3.dot(15)                           # Draw a dot at current position
    # Right eye
    t3.penup()
    t3.goto(-45, 10)
    t3.pendown()
    t3.dot(15)

    # Draw nose
    t3.pensize(5)
    t3.color("black", "white")
    t3.penup()
    t3.goto(-110, -20)
    t3.pendown()
    t3.begin_fill()
    t3.setheading(155)
    t3.circle(18, 240)                   # Left curve
    t3.circle(25, 25)
    t3.right(116)
    t3.circle(25, 25)                    # Right curve
    t3.circle(18, 240)
    t3.goto(-100, -20)
    t3.dot(20)                           # Draw nose tip as dot
    t3.end_fill()

main()