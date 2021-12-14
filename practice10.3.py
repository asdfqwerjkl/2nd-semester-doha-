#10장 연습문제 5번
from tkinter import *       #tkinter모듈을 불러온다
fields = '이름', '직업', '국적'
def fetch(entries):         #fetch를 정의한다
    for entry in entries:
        field = entry[0]
        text = entry[1].get()
        print('%s: "%s"' % (field, text)) 
def makeform(root, fields):     #makeform을 정의한다
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=15, text=field)      #GUI프레임에 보여짐
        ent = Entry(row)
        row.pack(side=TOP, fill=X)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((field, ent))
    return entries
root = Tk()             #윈도우 객체를 만든다
ents = makeform(root, fields)
root.bind('<Return>', (lambda event, e=ents: fetch(e))) 
b1 = Button(root, text='보여주기',command=(lambda e=ents: fetch(e)))#버튼생성위젯
b1.pack(side=LEFT, padx=5, pady=5)      #버튼1에 대한 psck()메소드 호출
b2 = Button(root, text='종료하기', command=root.quit)#버튼생성위젯
b2.pack(side=LEFT, padx=5, pady=5)      #버튼2에 대한 psck()메소드 호출
root.mainloop()             #무한대기문