import turtle

t = turtle.Turtle()
t.speed(3)

t.color("red")
t.fillcolor("red")

t.begin_fill()

t.left(140)
t.forward(180)

t.circle(-90, 200)
t.left(120)
t.circle(-90, 200)

t.forward(180)

t.end_fill()

t.penup()
t.goto(-50, -20)
t.color("Black")
t.write("I love myself", font=("Arial", 25, "bold"))

turtle.done()

