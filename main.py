import turtle

screen = turtle.Screen()


t = turtle.Turtle()

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("tan")

t.pencolor("blue")
t.penup()
t.goto(-80,15)
t.pendown()
t.circle(35)

t.pencolor("black")
t.penup()
t.goto(0,15,)
t.pendown()
t.circle(35)

t.pencolor("red")
t.penup()
t.goto(80,15,)
t.pendown()
t.circle(35)

t.pencolor("yellow")
t.penup()
t.goto(-40,-15,)
t.pendown()
t.circle(35)

t.pencolor("green")
t.penup()
t.goto(40,-15,)
t.pendown()
t.circle(35)

t.penup()
t.goto(0,100,)
t.pencolor("purple")
t.pendown()
t.write("Winter Olympics",font=("Arial",60,"normal"),align="center")

t.penup()
t.goto(0,-100,)
t.pencolor("purple")
t.pendown()
t.write("2026",font=("Arial",60,"normal"),align="center")





turtle.done()