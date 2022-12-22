import turtle
import time
import random

posponer = 0.1

score = 0
high_score = 0

wn = turtle.Screen()
wn.title("juego de la culebrita")
wn.bgcolor("black")
wn.setup(width= 600, height= 600)
wn.tracer(0)

cabeza = turtle.Turtle()
cabeza.speed(0)
<<<<<<< HEAD
=======
cabeza.shape("square")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "up"

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

while True:
    wn.update()

    mov()
>>>>>>> d9cbc6152e1475e9e5d8e3880c5c845c755f439c

