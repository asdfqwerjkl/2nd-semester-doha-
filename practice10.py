#10장 연습문제 1번
from tkinter import Tk, Label, Button

def greet():
    print("파이썬에 오신 것을 환영합니다.")
    
window = Tk()
label = Label(window,text = "간단한 GUI프로그램!")
label.pack()

greet_button = Button(window,text = "환영합니다.",command = greet)
greet_button.pack()

close_button=Button(window,text="종료",command = window.quit)
close_button.pack()

window.mainloop()

#10장 연습문제 2번
from tkinter import Tk,Label,Button,Entry,IntVar,END,W,E              

def update_add():
    update("add")

def update_subtract():
    update("subtract")
    
def update_reset():
    update("reset")
    
window = Tk()
total = 0
sum = Label(window)
sum.grid(row = 0,column = 1,columnspan = 2)

label = Label(window,text = "현재 합계:")
label.grid(row = 0,column = 0)

entry = Entry(window)
entry.grid(row = 1,column = 0,columnspan = 3)

add_button = Button(window,text = "더하기(+)",command = update_add)
subtract_button = Button(window,text = "뺴기(-)",command = update_subtract)
reset_button = Button(window,text = "초기화",command = update_reset)

add_button.grid(row = 2,column = 0)
subtract_button.grid(row = 2,column = 1)
reset_button.grid(row = 2,column = 2)

def update(method):
    global total
    if method =="add":
        total +=int(entry.get())
    elif method == "subtract":
        total -=int(entry.get())
    else:
        total = 0
    sum['text'] = str(total)
    entry.delete(0,END)
    
window.mainloop()

#10장 연습문제 3번
import random
from tkinter import*

window = Tk()
secret_number = random.randint(1,100)
guess = None
num_guesses = 0

def guess_number():
    global dum_guesses
    guess = int(entry.get())
    num_guesses +=  1
    if guess == secret_number:
        message = "축하합니다!"
    elif guess<secret_number:
        message = "너무 낮아요!"
    else:
        message = "너무 높아요!"
    label['text'] = message
        
def reset():
    global num_guesses
    entry.delete(0,END)
    secret_number = random.randint(1,100)
    guess = 0
    sum_guesses = 0
    message = "1부터 100사이의 숫자를 추측하시오"
    label['text'] = message
    
message = '1부터 100사이의 숫자를 추측하시오'
label = Label(window,text = message)
entry = Entry(window)
    
guess_button = Button(window,text = "숫자를 입력",cammand = guess_number)
guess_button = Button(window,text = "게임을 다시 실행",cammand = reset)

label.grid(row = 0,column = 0,columnspan = 2,sticky = W+E)
entry.grid(row = 1,column = 0,columnspan = 2,skicky = W+E)
guess_button.grid(eow = 2,column = 0)
reset_button.grid(eow = 2,column = 1)     

window.mainloop()
