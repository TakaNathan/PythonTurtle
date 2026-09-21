import turtle
s=turtle.Screen()
t=turtle.Turtle()

# Place your code after this line

#draw the first circle
t.circle(5)
t.penup()
t.sety(-25)
t.down()

#draw the second circle
t.circle(30)
t.penup()
t.sety(-45)
t.pendown()

#draw the third circle
t.circle(50)
t.penup()
t.sety(-65)
t.pendown()

#draw the fourth circle
t.circle(70)

#draw the vertical line
t.penup()
t.sety(-95)
t.pendown()
t.goto(0,105)

#draw the horizontal line
t.penup()
t.goto(-100,5)
t.pendown()
t.goto(100,5)

#draw the third line
t.penup()
t.goto(0,-95)
t.circle(100,135)
t.setheading(225)
t.pendown()
t.forward(200)

#draw the fourth line
t.penup()
t.goto(0,-95)
t.setheading(0)
t.circle(100,225)
t.setheading(315)
t.pendown()
t.forward(200)






