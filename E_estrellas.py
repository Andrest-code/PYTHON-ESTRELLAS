import turtle

turtle.title("EDUARDO CRACK")
a = turtle.Turtle()
a.getscreen().bgcolor("black")
a.penup()
a.goto(-215, 50)
a.pendown()
a.color("#AACDE2")
a.speed(25)

def star(turtle, size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for _ in range(5):
            turtle.forward(size)
            star(turtle, size / 3)
            turtle.left(216)
        turtle.end_fill()

# Función para dibujar el nombre "EDUARDO CRACK"
def draw_name():
    turtle.penup()
    turtle.goto(-50, -220)
    turtle.color("#AACDE2")
    turtle.write("EDUARDO CRACK", align="center", font=("Arial", 20, "normal"))

def zoom_and_rotate():
    for _ in range(36):
        a.clear()
        a.left(10)
        star(a, 380 - 10 * _)
        draw_name()  # Llama a la función para dibujar el nombre en cada iteración
        turtle.update()

zoom_and_rotate()
turtle.done()
