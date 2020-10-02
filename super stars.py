import turtle

kim = turtle.Turtle()
kim.getscreen().bgcolor("#994444")

kim.penup()
kim.goto((-200, 100))
kim.pendown()
kim.speed(0)


def star(turtle, size):
    if size <=5:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            star(turtle, size/2)
            turtle.left(216)
        turtle.end_fill()

star(kim, 330)



turtle.done()
