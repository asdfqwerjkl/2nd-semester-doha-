print("나는"+str(12)+"개의 사과를 먹었다")

str = input("문자열을 입력하시오:")     #처음 두글자와 마지막 두글자를 쓰는 함수
s = str[0:2]+str[-2:]
print(s)

s = input("문자열을 입력하시오:")
s+="하는중"
print(s)

str = input("기호를 입력하시오:")       #기호1개 쓰고 단어 쓰고 나머지 기호쓰는 함수
word = input("중간에 삽입할 문자열을 입력하시오?:")
s = str[:1]+word+str[1:]

print(s)

lista = [1,2,3,4]
sum = 0
sum = lista[0]+lista[1]+lista[2]+lista[3]
print("리스트=",lista)
print("리스트 숫자들의 합=",sum)

import turtle           
t = turtle.Turtle()
t.shape("turtle") 

lista = [ ]

color = input("색상 #1을 입력하시오:")
lista.append(color)
color = input("색상 #1을 입력하시오:")
lista.append(color)
color = input("색상 #1을 입력하시오:")
lista.append(color)

t.fillcolor(lista[0])
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.goto(100,0)
t.down()
t.fillcolor(lista[1])
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.goto(200,0)
t.down()
t.fillcolor(lista[2])
t.begin_fill()
t.circle(50)
t.end_fill()
t._screen.exitonclick()      #화면을 마우스로 클릭해야 종료되게 하는 부분

from turtle import 
shape("turtle")

lista = [ ]

color = input("색상 #1을 입력하시오:")
lista.append(color)
color = input("색상 #1을 입력하시오:")
lista.append(color)
color = input("색상 #1을 입력하시오:")
lista.append(color)


fillcolor(lista[0])
begin_fill()
circle(50)
end_fill()

up()
goto(100,0)
down()
fillcolor(lista[1])
begin_fill()
circle(50)
end_fill()

up()
goto(200,0)
down()
fillcolor(lista[2])
begin_fill()
circle(50)
end_fill()

write("닫으려면 화면 클릭")
exitonclick()     #화면을 마우스로 클릭해야 종료되게 하는 부분

import turtle           
t = turtle.Turtle()
t.shape("turtle") 

lista = [ ]
lista.append(int(input("x1:")))
lista.append(int(input("y1:")))
lista.append(int(input("x2:")))
lista.append(int(input("y2:")))
lista.append(int(input("x3:")))
lista.append(int(input("y3:")))

t.goto(lista[0],lista[1])
t.goto(lista[2],lista[3])
t.goto(lista[4],lista[5])
t._screen.exitonclick()      #화면을 마우스로 클릭해야 종료되게 하는 부분

from turtle import 
shape("turtle")

lista = [ ]
lista.append(int(input("x1:")))
lista.append(int(input("y1:")))
lista.append(int(input("x2:")))
lista.append(int(input("y2:")))
lista.append(int(input("x3:")))
lista.append(int(input("y3:")))

goto(lista[0],lista[1])
goto(lista[2],lista[3])
goto(lista[4],lista[5])

write("닫으려면 화면 클릭")
exitonclick()     #화면을 마우스로 클릭해야 종료되게 하는 부분
