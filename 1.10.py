from tkinter import *       #tkinter모듈을 불러온다
def process():              #process를정의한다.
    temperature = float(e1.get())   #실수형변수
    mytemp = (temperature-32)*5/9   #mytemp변수의 숫자 계산
    e2.insert(0, str(mytemp))        #리스트 형태의 데이터에 원하는 위치와원하는 값을 추가
def process2():             #process2을 정의한다
    temperature = float(e2.get())   #실수형변수
    mytemp = (temperature*(9/5))+32 #mytemp변수의 숫자 계산
    e1.insert(0, str(mytemp))       #리스트 형태의 데이터에 원하는 위치와원하는 값을 추가
window = Tk()                       #TK클래스가 윈도우를 나타낸다
l1 = Label(window, text = "화씨")   #GUI프레임에 보여짐
l2 = Label(window, text = "섭씨")   #GUI프레임에 보여짐
l1.grid(row = 0, column = 0)        #위치
l2.grid(row = 1, column = 0)        #위치
e1 = Entry(window)          #글자를 입력할 수 있는 창
e2 = Entry(window)          #글자를 입력할 수 있는 창
e1.grid(row = 0, column = 1)        #위치
e2.grid(row = 1, column = 1)        #위치
b1 = Button(window, text = "화씨 -> 섭씨", command=process)     #버튼생성위젯
b2 = Button(window, text = "섭씨 -> 화씨", command=process2)    #버튼생성위젯
b1.grid(row = 2, column = 0)        #위치
b2.grid(row = 2, column = 1)        #위치
window.mainloop()       #무한루프문

#도전문제.Chapter10.page295(1)
from tkinter import *       #TKINTER모듈을 불러온다
window = Tk()       #TK클래스가 윈도우를 나타낸다
w = Button(window, text = "버튼1", bg="red", fg="white")    #버튼생성위젯(배경 붉은색, 버튼색 흰색)
w.place(x=0, y=0) #위치
w = Button(window, text = "버튼2", bg="orange", fg="white")#버튼생성위젯(배경 오랜지색, 버튼색 흰색)
w.place(x=20, y=20) #위치
w = Button(window, text = "버튼3", bg="yellow", fg="white")#버튼생성위젯(배경 노란색, 버튼색 흰색)
w.place(x=40, y=40) #위치
w = Button(window, text = "버튼4", bg="green", fg="white")#버튼생성위젯(배경 초록색, 버튼색 흰색)
w.place(x=60, y=60) #위치
w = Button(window, text = "버튼5", bg="blue", fg="white")#버튼생성위젯(배경 파란색, 버튼색 흰색)
w.place(x=80, y=80) #위치
window.mainloop()   # 무한루프문


from tkinter import *   #tkinter모듈을 불러온다
def paint(event):       #paint정의
    global lastx, lasty #전역함수
    x, y = (event.x),(event.y)
    canvas.create_line(lastx,lasty,x,y,fill = "black")
    lastx,lasty = x,y
def activate_paint(event):  #activate_paint 정의
    global lastx, lasty #전역함수
    lastx, lasty = (event.x),(event.y) 
def release(event):         #release 정의
    global lastx, lasty #전역함수
    if (lastx, lasty) == (event.x,event.y):     #가정문
        canvas.create_line(lastx,lasty,lastx+1,lasty+1)
lastx,lasty = None, None
window = Tk()           #TK클래스가 윈도우를 나타낸다
canvas = Canvas(window)
canvas.pack()       #pack()메소드를 호출한다
canvas.bind('<B1-Motion>',paint)
canvas.bind('<ButtonPress-1>', activate_paint) #B1-Press
canvas.bind('<ButtonRelease-1>',release) #B1-Release
window.mainloop()   # 무한루프문


from tkinter import *
mycolor = "blue" #mycolor변수 생성
def paint(event):   #paint정의
    x1,y1 = (event.x-1), (event.y+1)
    x2,y2 = (event.x-1), (event.y+1)
    canvas.create_oval(x1, y1, x2, y2, fill = mycolor)
def change_color_red(): #change_color_red
    global mycolor      #전역변수
    mycolor = "red"     #mycolor변수 바꾸기(?->red)
def change_color_green():   #change_color_green
    global mycolor      #전역변수
    mycolor = "green"   #mycolor변수 바꾸기(?->green)
def change_color_yellow():  #change_color_yellow
    global mycolor      #전역변수
    mycolor = "yellow"  #mycolor변수 바꾸기(?->yellow)
window = Tk() #Tk클래스가 윈도우를 나타낸다
canvas = Canvas(window)
canvas.pack()   #캔버스에 대한 pack()메소드를 불러온다
canvas.bind("<B1-Motion>", paint)
button = Button(window, text="빨간색", command=change_color_red) #버튼위젯생성-빨간색
button.pack() #버튼에 대한 pack()메소드를 불러온다
button = Button(window, text="녹 색", command=change_color_green)#버튼위젯생성-녹색
button.pack()#버튼에 대한 pack()메소드를 불러온다
button = Button(window, text="노란색", command=change_color_yellow)#버튼위젯생성-노란색
button.pack()#버튼에 대한 pack()메소드를 불러온다
window.mainloop() # 무한루프문