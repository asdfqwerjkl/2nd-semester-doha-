#9장 연습문제 3번
contacts = {}
while True: 
    name = input("(입력모드)이름을 입력하시오:")
    if not name: 
        break;
    tel = input("전화번호를 입력하시오:")
    contacts[name] = tel
while True:
    name2 = input("(검색모드)이름을 입력하시오:")
    print(name2,"의 전화번호는",contacts[name2],"입니다.")
    if not name2:
        break;

#9장 연습문제 4번
import random
import turtle
t = turtle.Turtle()
t.shape("turtle")
color = ["yellow","red","purple","blue"]
def draw_square(x,y,c):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(c)
    t.begin_fill(4):
    for i in range(4):
        t.fd(50)
        t.lt(90)
    t.end_fill
for c in color:
    x = random.randint(-100,100)
    y = random.randint(-100,100)
    draw_spuare(x,y,c)
