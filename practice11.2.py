#11장 연습문제 5번
import pickle       #pickle 모듈 가져오기
outfile = open("test.dat", "wb")    #출력파일열기,b추가
pickle.dump(12, outfile)        #정수저장
pickle.dump(3.14, outfile)      #실수저장
pickle.dump([1, 2, 3, 4, 5], outfile)   #리스트 저장
outfile.close()                     #출력파일 닫기
infile = open("test.dat", "rb")     #입력파일 열기,b추가
print(pickle.load(infile))
print(pickle.load(infile))
print(pickle.load(infile))
infile.close()                      #입력파일 닫기

#11장 연습문제 6번
inFileName = input("입력 파일 이름: ")#입력파일이름 입력
outFileName = input("출력 파일 이름: ") #출력파일 이름 입력
infile = open(inFileName, "r")      #입력을 위한 파일 열기,b붙여줌
outfile = open(outFileName, "w")    #출력을 위한 파일 열기,b붙여줌
total = 0.0         #total변수 생성
count = 0           #count변수 생성
line = infile.readline()    #파일 읽기
while line != "" :
    value = float(line)     
    total = total + value
    count = count + 1
    line = infile.readline()
outfile.write("합계="+ str(total)+"\n")
avg = total / count     #평균값계산
outfile.write("평균="+ str(avg)+"\n")   
infile.close()      #파일닫기
outfile.close()     #파일닫기

#11장 연습문제 7번
import pickle           #pickle모듈을 불러온다
from tkinter import *   #tkinter모듈을 불러온다
phone_book = { }
current = 0         #current변수 생성
name = ""           #name변수 생성(아무것도 없다)
phone = ""          #phone변수 생성(아무것도 없다)
window = Tk()       #Tk클래스가 윈도우를 나타낸다
#프레임에 글자를 만드는 구간
frame1 = Frame(window)
frame1.pack()
Label(frame1, text = "이름 ").grid(row = 1, column = 1, sticky = W)
nameEntry = Entry(frame1, textvariable = name, width = 30)
nameEntry.grid(row = 1, column = 2)
frame2 = Frame(window)
frame2.pack()
Label(frame2, text = "전화번호").grid(row = 1, column = 1, sticky = W)
phoneEntry = Entry(frame2, textvariable = phone, width = 30)
phoneEntry.grid(row = 1, column = 2)
frame3 = Frame(window)
frame3.pack()
def save():     #save 정의
    outfile = open("phonebook.dat", "wb")
    pickle.dump(phone_book, outfile)
    print("주소들이 파일에 저장되었습니다")
    outfile.close()
def load():     #load 정의
    infile = open("phonebook.dat", "rb")
    phone_book = pickle.load(infile)
    infile.close()
    print("파일에서 주소를 읽었습니다.")
    go_first()
def add():      #add정의
    phone_book[nameEntry.get()] = phoneEntry.get()
    print(phone_book)
    save()
def go_first(): #go_first 정의
    global current
    current = 0
    ks = list(phone_book)
    print(phone_book)
    nameEntry.delete(0, END)
    nameEntry.insert(0, ks[current])
    phoneEntry.delete(0, END)
    phoneEntry.insert(0, phone_book[ks[current]])
def go_next():  #go_next 정의
    global current
    current += 1
    ks = list(phone_book)
    nameEntry.delete(0, END)
    nameEntry.insert(0, ks[current])
    phoneEntry.delete(0, END)
    phoneEntry.insert(0, phone_book[ks[current]])
def go_previous():          #go_previous 정의
    print("구현되지 않았음")    #출력
def go_last():
    print("구현되지 않았음")       #출력
    
b1 = Button(frame3, text = "추가", command = add).grid(row = 1, column = 1) #버튼1생성위젯,위치
b2 = Button(frame3, text = "처음", command = go_first).grid(row = 1, column = 2)#버튼2생성위젯,위치
b3 = Button(frame3, text = "다음", command = go_next).grid(row = 1, column = 3)#버튼3생성위젯,위치
b4 = Button(frame3, text = "이전", command =go_previous).grid(row = 1, column = 4)#버튼4생성위젯,위치
b5 = Button(frame3, text = "마지막", command = go_last).grid(row = 1, column = 5)#버튼5생성위젯,위치
b6 = Button(frame3, text = "파일 읽기", command = load).grid(row = 1, column = 6)#버튼6생성위젯,위치
window.mainloop() # 무한루프문