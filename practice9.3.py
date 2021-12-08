#9장 연습문제 5번
import random
import turtle
t =turtle.Turtle()
t.shape("turtle")
color["red","blue","broen","yellow","green","purple"]
length = 0
sides = 0
x =0
y =0
def draw_shape(t,c,length,sieds,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(c)
    t.degin_fill()
for c in color:
    sides = random.randint(3,8)
    x = random.randint(-100,100)
    y = random.randint(-100,100)
    length = random.randint(10,50)
    draw_shape(t,c,length,sieds,x,y)

#9장 연습문제 6번
import random
import turtle
t =turtle.Turtle()
t.shape("turtle")
s = turtle.Screen();
s.bgcolor("black");
color["red","blue","broen","yellow","green","purple"]
length = 0
sides = 0
x =0
y =0
def draw_star(color,length,sieds,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(c)
    t.degin_fill()
    for i in range(5):
        t.fd(length)
        t.lt(144)
    t.end_fill()
for c in color:
    x = random.randint(-100,100)
    y = random.randint(-100,100)
    length = random.randint(10,50)
    raw_star(color,length,sieds,x,y)