# Drawing Ryan using Python Turtle
# Source: https://m.blog.naver.com/runpython/222913719381
import turtle

# Set colors
bg_color = "lightcyan"
line_color = "black"
body_color = "#f0a53a"    #"#edaa4e"   #"orange"
nose_color = "white"
chest_color = "white"

s = turtle.Screen()
s.setup(650, 800)
s.bgcolor(bg_color)
t = turtle.Turtle()
t.pensize(5)
t.speed(3)
print(s.tracer())
#s.tracer(0)

# Draw body
# Coordinate order: left top (x,y), left bottom, right bottom, right top
posbody = [(-90,20),(-90,-150),(90,-150),(90,20),      # Black outline (0)
           (-85,20),(-85,-145),(85,-145),(85,20)]      # Orange inside (1)
def drawbody(col):
    if col == 0:      # Black outline
        t.color(line_color, line_color)
    elif col == 1:    # Orange inside
        t.color(body_color, body_color)
    t.penup()
    t.goto(posbody[col*4+0])     
    t.pendown()
    t.begin_fill()
    t.goto(posbody[col*4+1])      
    t.goto(posbody[col*4+2])       
    t.goto(posbody[col*4+3])      
    t.end_fill()

# Draw leg
# Coordinate order: left top (x,y), left bottom, right bottom, right top
posleg = [(-90,-140),(-90,-170),(-20,-170),(-20,-140),  # Black outline left (0,0)
          (90,-140),(90,-170),(20,-170),(20,-140),      # Black outline right (0,1)
          (-85,-140),(-85,-170),(-25,-170),(-25,-140),  # Orange left (1,0)
          (85,-140),(85,-170),(25,-170),(25,-140)]      # Orange right (1,1)
def drawleg(col, d): 
    if col == 0:      # Black outline
        t.color(line_color, line_color)
    elif col == 1:    # Orange inside
        t.color(body_color, body_color)
    t.penup()
    t.goto(posleg[col*8+d*4 + 0])
    t.begin_fill()
    t.pendown()
    t.goto(posleg[col*8+d*4 + 1])   
    t.goto(posleg[col*8+d*4 + 2])   
    t.goto(posleg[col*8+d*4 + 3])   
    t.end_fill()

# Draw feet
posfoot = [(-55, -170),     # Left (0)
           (55, -170)]      # Right (1)
def drawfoot(col, d):
    t.penup()
    t.goto(posfoot[d])
    if col == 0:      # Black outline
       t.dot(75, line_color)
    elif col == 1:    # Orange inside
        t.dot(65, body_color)

# Draw hands
poshand = [(-45, -40),     # Left (0)
           (45, -40)]     # Right (1)
def drawhand(col, d):
    t.penup()
    t.goto(poshand[d]) 
    if col == 0:      # Black outline
       t.dot(150, line_color)
    elif col == 1:    # Orange inside
       t.dot(140, body_color)  

# Draw separation lines between hands and body
posline = [(-90, -30),(-90, -100),     # Left (0)
           (90, -30),(90, -100)]       # Right (1)
def drawhandline(d):
    t.pencolor(line_color)
    t.penup()
    t.goto(posline[d*2 + 0])
    t.pendown()         
    t.goto(posline[d*2 + 1])

# Draw chest tulip pattern
poschest = [(40,-40),(20,-60),(0,-40),(-20,-60),(-40,-40)] # Zig-zag positions