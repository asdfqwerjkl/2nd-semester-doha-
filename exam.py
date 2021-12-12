#자동차 머시기
class Car:
    def __init__(self,model,speed,color):
        self.model = model 
        self.speed = speed 
        self.color = color        
    def __del__(self):
        print("인스턴스를 소멸합니다.")
    def show_info(self):
        print("속도:",self.speed,"/모델:",self.model,"/색상:",self.color)
car1 = Car("람보르기니","100마하","무지개색")
car1.show_info()
del car1

#학생의 점수
x = int(input("점수를 입력하시오"))
if x >=90:
    print("당신의 점수는 A입니다.")
elif x>=80:
    print("당신의 점수는 B입니다.")
elif x>=80:
    print("당신의 점수는 C입니다.")
elif x>=80:
    print("당신의 점수는 D입니다.")    
else: 
    print("당신의 점수는 F입니다.")    

#2단부터 9단까지
x = 2
while x<=9:
    y = 1
    while y <=9:
        print(x,"*",y"=",x*y)
        y+=1
    x+=1

#9단만
x = 9
y = 1
while y <=9:
    print(x,"*",y,"=",x*y)
    y+=1
    
#GUI머시기
from tkinter import*        #내장함수를 가져온다
                            #가독성을 위해 한줄 띄운다
window = Tk()               #Tk클래스가 윈도우를 나타낸다.
button = button(window,text = "클릭하시오.")#버튼생성위젯(위치,속성)
button.pack()               #pack()메소드를 호출한다
                            #가독성을 위해 한줄 띄운다.
window.mainloop()           #윈도우에서 발생하는 이벤트를 처리한다. 무한대기문