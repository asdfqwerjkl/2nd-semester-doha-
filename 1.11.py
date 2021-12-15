from tkinter import *       #tkinter모듈을 불러온다
import random               #랜덤모듈을 불러온다
def show(char):             #show를 정의한다
    display.delete(0,END)
    display.insert(0,"단어를 추측하시오:")
    global blanked
    blanked = 0
    global guesses
 
    for char in word:
        if char in guesses:
            display.insert(END,char)
        else:
            display.insert(END,"_ ")
            blanked += 1
def click(char):
    show(char)
    global turns
    global label 
    global blanked
 
    if blanked == 0:
        label = Label(root, text = "사용자 승리",width = 20, height=1, fg="red", relief="solid")
        label.grid(row=row_index,column=col_index,columnspan=5)
        chooseWord()
        return
    if char not in word:
        turns -= 1
        label = Label(root,text=str(turns)+"번의 기회가 남았음!", width=20, height=1, fg="red", relief="solid")
        label.grid(row=row_index,column=col_index, columnspan=5)
    if turns <= 0:
        label = Label(root, text = "사용자 패배", width = 20, height=1, fg = "red", relief = "solid")
        label.grid(row=row_index, column = col_index, columnspan=5)
        chooseWord()
        return
def chooseWord():
    global word
    global turns
    turns = 10
    global guesses
    guesses = ""
    global label 
    label = Label(root,text=str(turns)+"번의 기회가 남았음!", width=20, height=1, fg="red", relief="solid")
    infile = open("words.txt","r")
    lines = infile.readlines()
    word = random.choice(lines)
    word = word.replace(" ","")
    word = word.replace("\n","")
    show("")
root = Tk()
root.title("Hangman Game")
root.geometry("300x225")
display = Entry(root, width=33, bg="yellow")
display.grid(row=0,column=0,columnspan=5)
guesses = "" 
turns = 10
word=""
chooseWord()
button_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
row_index=1
col_index=0
blanked = 0
display.delete(0,END)
display.insert(0,"단어를 추측하시오:")
show("")
for button_text in button_list:
    def process(guess=button_text):
        global guesses
        global turns
        guesses += guess
        click(guess)
Button(root,text=button_text,width=5,command=process).grid(row=row_index,column=col_index)
    col_index += 1
    if col_index > 4:
        row_index += 1
        col_index = 0
row_index += 1
root.mainloop()

import pickle       #pickle모듈 불러오기
# 게임에서 사용되는 딕셔너리
addressBook = {"names":["김김김","이이이","박박박","홍길동"],"mails":["aaa@gmail.com","bbb@gmail.com","ccc@gmail.com","ddd@gmail.com"],"address":["seoul","daejeon","daegu","busan"]}
# 이진 파일 오픈
file = open("save.p","wb")
# 딕셔너리를 피클 파일에 저장
pickle.dump(addressBook,file)
# 파일을 닫는다. file.close()
# 이진 파일 오픈
file = open("save.p","rb")
# 피클 파일에 딕셔너리를 로딩
obj = pickle.load(file)
print(obj)



from PIL import Image, ImageTk, ImageFilter
import tkinter as tk
from tkinter import filedialog as fd
im = None
tk_img = None
# 파일 메뉴에서 "열기"를 선택하였을 때 호출되는 함수
def open():
    global im, tk_img
    fname = fd.askopenfilename()
    im = Image.open(fname)
    tk_img = ImageTk.PhotoImage(im)
    canvas.create_image(250,250,image=tk_img)
    window.update()
# 파일 메뉴에서 "종료"를 선택하였을 때 호출되는 함수
def quit():
    window.quit()
# 영상처리 메뉴에서 "영상회전"을 선택하였을 때 호출되는 함수
def image_rotate():
    global im, tk_img
    out = im.rotate(45)
    tk_img = ImageTk.PhotoImage(out)
    canvas.create_image(250,250,image=tk_img)
    window.update()
# 영상처리 메뉴에서 "영상흐리기"를 선택하였을 때 호출되는 함수
def image_blur():
    global im, tk_img
    out = im.filter(ImageFilter.BLUR)
    tk_img = ImageTk.PhotoImage(out)
    canvas.create_image(250,250,image=tk_img)
    window.update()
# 영상처리 메뉴에서 "흑백영상"를 선택하였을 때 호출되는 함수
def image_grayscale():
    global im, tk_img
    im1 =im.convert('L')
    tk_img = ImageTk.PhotoImage(im1)
    canvas.create_image(250,250,image=tk_img)
    window.update()
# 영상처리 메뉴에서 "이진화"를 선택하였을 때 호출되는 함수
def image_bin():
    global im, tk_img
    im1 =im.convert('1')
    tk_img = ImageTk.PhotoImage(im1)
    canvas.create_image(250,250,image=tk_img)
    window.update()
# 영상처리 메뉴에서 "영상뚜렷하게"를 선택하였을 때 호출되는 함수
def image_sharp():
    global im, tk_img
    out = im.filter(ImageFilter.SHARPEN)
    tk_img = ImageTk.PhotoImage(out)
    canvas.create_image(250,250,image=tk_img)
    window.update()
# 영상처리 메뉴에서 "엠보스"를 선택하였을 때 호출되는 함수
def image_emboss():
    global im, tk_img
    out = im.filter(ImageFilter.EMBOSS)
    tk_img = ImageTk.PhotoImage(out)
    canvas.create_image(250,250,image=tk_img)
    window.update()
# 윈도우를 생성한다. window = tk.Tk()
canvas = tk.Canvas(window,width=500,height=500)
canvas.pack()
# 메뉴를 생성한다. menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
ipmenu = tk.Menu(menubar)
filemenu.add_command(label="열기", command = open)
filemenu.add_command(label="종료", command = quit)
ipmenu.add_command(label="영상회전", command=image_rotate)
ipmenu.add_command(label="영상흐리게", command=image_blur)
ipmenu.add_command(label="흑백영상", command=image_grayscale)
ipmenu.add_command(label="이진화", command=image_bin)
ipmenu.add_command(label="영상뚜렷하게", command=image_sharp)
ipmenu.add_command(label="엠보스", command=image_emboss)
menubar.add_cascade(label="파일",menu=filemenu)
menubar.add_cascade(label="영상처리",menu=ipmenu)
window.config(menu=menubar)
window.mainloop()