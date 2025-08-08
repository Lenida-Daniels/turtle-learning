import turtle

# create a screen/window
wn= turtle.Screen()
wn.bgcolor("skyblue")
wn.title("Code shapes with @Daniels")
wn.setup(width= 600, height= 600)

#create a pen
pen= turtle.Turtle()
pen.pensize(3)
pen.speed(3)

# Function to draw a square
def draw_square(size):
    pen.begin_fill()
    for _ in range(4):
        pen.forward(size)
        pen.right(90)
        
    pen.end_fill()

#function to draw a triangle
def draw_triangle(size):
    pen.begin_fill()
    for _ in range(3):
        pen.forward(size)
        pen.right(120)
    pen.end_fill()

# Square
pen.penup()
pen.goto(-250, 250)
pen.pendown()
pen.color("black","pink")
pen.write("Square",font=("Arial", 16, "bold"))
draw_square(100)

#triangle
pen.penup()
pen.goto(-100, 250)
pen.pendown()
pen.color("black")
draw_triangle(100)
pen.hideturtle()
pen.write("Triangle",font=("Arial", 16, "bold"))


turtle.done()