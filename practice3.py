x= int(input("x:"))
y = int(input("y:"))
print("두수의합:",x+y)
print("두수의차:",x-y)
print("두수의곱:",x*y)
print("두수의평균:",(x+y)/2)
print("큰수:",max(x+y))
print("작은수:",min(x+y))

r = float(input("r:"))
h = float(input("h:"))

vol = 3.141592*r**2*h
print("원기둥의 부피:",vol)

number = int(input("정수를 입력하시오:"))

sum =0
sum = sum +number%10
sumber = number//10
sum = sum +number%10
sumber = number//10
sum = sum +number%10
sumber = number//10
sum = sum +number%10
sumber = number//10
print("자리수의 합:",str(sum),str(sum))

x1 = int(input("x1:"))
y1 = int(input("y1:"))
x2 = int(input("x2:"))
y2 = int(input("y2:"))
dist = ((x2-x1)**2+(y2-y1)**2)**0.5
print("두점 사이의 거리=",dist)

import math
x1 = int(input("x1:"))
y1 = int(input("y1:"))
x2 = int(input("x2:"))
y2 = int(input("y2:"))
dist = math.sqrt((x2-x1)**2+(y2-y1)**2)
print("두점 사이의 거리=",dist)

import turtle           
t = turtle.Turtle()
t.shape("turtle") 

t.left(45)
t.forward(141)
t.setheading(0)
t.goto(0,0)
t.forward(100)
t.left(90)
t.forward(100)
t._screen.exitonclick()      #화면을 마우스로 클릭해야 종료되게 하는 부분

from math import
x1 = int(input("x1:"))
y1 = int(input("y1:"))
x2 = int(input("x2:"))
y2 = int(input("y2:"))
dist = sqrt((x2-x1)**2+(y2-y1)**2)
print("두점 사이의 거리=",dist)

from turtle import 
shape("turtle")

left(45)
forward(141)
setheading(0)
goto(0,0)
forward(100)
left(90)
forward(100)
write("닫으려면 화면 클릭")
exitonclick()               #화면을 마우스로 클릭해야 종료되게 하는 부분


import turtle           
t = turtle.Turtle()
t.shape("turtle") 

x1 = int(input("x1:"))
y1 = int(input("y1:"))
x2 = int(input("x2:"))
y2 = int(input("y2:"))
dist = ((x2-x1)**2+(y2-y1)**2)**0.5

t.up()
t.goto(x1,y1)
t.down()
t.doto(x2,y2)

t.wrtie("점의 길이"+str(dist))
t._screen.exitonclick()      #화면을 마우스로 클릭해야 종료되게 하는 부분



from turtle import 
shape("turtle")

x1 = int(input("x1:"));y1 = int(input("y1:"))
x2 = int(input("x2:"));y2 = int(input("y2:"))
dist = ((x2-x1)**2+(y2-y1)**2)**0.5
up(); goto(x1,y1);down();goto(x2,y2)

write("점의 길이=",str(dist))

exitonclick()      #화면을 마우스로 클릭해야 종료되게 하는 부분


import time

fseconds= time.time() - starttime
totla_sec = int(fseconds)
total_min = total_sec //60

minute = total_min%60
total_hour = total_min //60
hour = total_hour%24

print("현재 시간(영국 그리니치 시각):"+str(hour)+"시"+str(minute)+"분")

mass = float(input("물체의 무게를 입력하시오(킬로그램):"))
velocity = float(input("물체의 속도를 입력하시오(미터/초):"))

ecergy = 0.5*mass*velocity**2    
print("물체는 "str(energy)+"(줄)의 에너지를 가지고 있다."