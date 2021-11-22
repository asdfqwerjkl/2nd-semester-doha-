#7번 연습문제

import turtle
t= turtle.Turtle() 
t.shape("turtle") 
t.color("blue")

t.left(90)
for i in range(6):
    t.left(60); t.forward(100); t.forward(-30); t.left(60); t.forward(30); t.forward(-30); t.right(120); t.forward(30); t.forward(-30); t.left(60); t.back(70)
    
t.screen.exitonclick()

#8번 연습문제

import turtle 
t= turtle.Turtle() 
t.color("red")
t.speed(50)
t.left(180)
for i in range(10):
    t.left(10)
    t.fd(200)
    t.right(144)
    t.fd(200)
    t.right(144)
    t.fd(200)
    t.right(144)
    t.fd(200)
    t.right(144)
    t.fd(200)
    t.right(144)

t.screen.exitonclick()

#9번 문제 
import turtle 
import random 
t = turtle.Turtle() 
t.shape("turtle")
t.speed(20)
for i in range(10): 
    r = random.randint(1,100)
    x = random.randint(-100,100)
    y = random.randint(-100,100)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(r)
    
t.screen.exitonclick()

#10번 문제 
import turtle 
t= turtle.Turtle()
t.shape("turtle")
t.speed(20)
for i in range(5): 
    t.forward(200)
    t.right(90)
    t.fd(20)
    t.right(90)
    t.forward(200)
    t.left(90)
    t.fd(20)
    t.left(90)
    
t.screen.exitonclick()

#11번 문제
'''
t.color(x,y)에서 x는 선의 색, y는 도형안의 색을 말한다. 
또한 t.begin_fill()은 도형안의 색을 채우는 것이고 t.end_fill()은 색을 채우는 것을 하지않는다는 것이다. 
abs = 절댓값
t.pos = 거북이의 좌표 
if abs(t.pos())<1 = '거북이의 x,y값중 하나의 절댓값이 1보다 작아지면'이라는 뜻이다.
'''

#12번 문제
