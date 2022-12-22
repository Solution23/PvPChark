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

