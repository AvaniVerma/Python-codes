import turtle

def draw_shape(arrow):
   arrow.left(30)
   arrow.forward(50)
   arrow.right(60)
   arrow.forward(50)
   arrow.right(120)
   arrow.forward(50)
   arrow.right(60)
   arrow.forward(50)
 

def draw():
    window = turtle.Screen()
    arrow = turtle.Turtle()
    arrow.speed(50)
   # draw_shape(arrow)
    for i in range(1, 75):
        draw_shape(arrow)
        arrow.right(5)
    stem=turtle.Turtle()
    stem.right(90)
    stem.forward(200)
    window.exitonclick()

draw()
