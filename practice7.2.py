#연습문제 2번 
import turtle
t = turtle.Turtle() 
t.shape("turtle")
def hexagon():
    for i in range(6): 
        t.forward(100)
        t.left(360/6)
for i in range(6): 
    hexagon()
    t.fd(100)
    t.right(60)
    
#연습문제 3번 
import turtle 
import math 
t = turtle.Turtle 
t.shape("turtle")
t.speed(10000)
t.fd(10000)
t.right(180)
t.fd(10000)
t.left(90)
t.fd(10000)
t.right(180)
t.fd(10000)
t.speed(10)
for x in range(150): 
    y = math.x^2+1
    t.goto(x,y)
    