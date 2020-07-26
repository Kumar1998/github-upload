import turtle
turtle.bgcolor("grey")
turtle.pensize(3)
turtle.speed(0)

for i in range(8):
    for colours in ['orange','pink','violet','red','cyan','violet','gold']:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(15)
turtle.hideturtle()
    
        

        