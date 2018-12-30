import turtle


#if loop range is (1,4), it draws a star
def draw_square(arrow):
    for i in range(1,5):
        arrow.forward(100)
        arrow.right(90)
        


def draw():
    window = turtle.Screen()
    window.bgcolor("Aqua")

    arrow = turtle.Turtle()
    arrow.speed(5)
    for i in range(0,36):
        draw_square(arrow)
        arrow.right(10)

    window.exitonclick()


draw()
