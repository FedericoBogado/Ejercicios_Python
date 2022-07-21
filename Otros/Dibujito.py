import turtle
import colorsys


def run():
    t = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor('black')
    t.speed(0)
    n = 80
    h = 0

    for i in range (302):
        c = colorsys.hsv_to_rgb(h, 1, 0.8)
        h = h + 1/n
        t.color(c)
        t.left(104)
        t.forward(i*3)
        
        for j in range (2):
            t.left(5)
            t.forward(i*2)
            t.left(52)


if __name__ == "__main__":
    run()