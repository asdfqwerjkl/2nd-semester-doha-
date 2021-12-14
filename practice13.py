#13장 연습문제 1번
class Circle:       #원을 나타내는 클래스 정의
    def __init__(self, radius):     #인스턴스 생성
        self.radius = radius
    def calcPerimeter(self):        #calcPerimeter정의
        return 2 * 3.141592 * self.radius #계산
    def calcArea(self):        #calcArea정의
        return 3.141592* self.radius*self.radius #계산
circle = Circle(100)    #반지름 100인 원을 클래스를 이용해 만듦
print("반지름: ", circle.radius,"원의 면적: ", circle.calcArea(),"원의 둘레: ", circle.calcPerimeter() ); # 출력

#13장 연습문제 2번
class TV:       #TV을 나타내는 클래스 정의
    def __init__(self):     #인스턴스 생성
        self.channel = 1
        ...
    def turnOn(self):           #turnOn 정의
        ...

class TV: #TV을 나타내는 클래스 정의
    def __init__(self): #인스턴스 생성
        self.channel = 1
        self.volume = 0 
        self.on = False 
    def turnOn(self):   #turnOn 정의
        self.on = True
    def turnOff(self):  #turnOff 정의
        self.on = False
    def setVolume(self, volume):    #setVolume 정의
        self.volume = volume
    def setChannel(self, channel):  #setChannel 정의
        self.channel = channel
tv = TV() # TV클래스를 이용해 생성
tv.turnOn() #위의 turnOn 정의사용
tv.setChannel(11)#위의 setChannel 정의사용
tv.setVolume(6)#위의 setVolume 정의사용
print("TV의 채널: ", tv.channel, "TV의 음량:", tv.volume); # 출력

#13장 연습문제 3번
import turtle       #터틀모듈을 불러온다
lee = turtle.Pen()  #펜생성(?)
park = turtle.Pen() #펜생성(?)
lee.shape("turtle")#펜모양은 거북이
lee.forward(100)#100픽셀만큼 전진
lee.right(90)   #오른쪽으로 90도 회전
lee.forward(20) #20픽셀만큼 전진
lee.left(90)    #왼쪽으로 90도 회전
lee.forward(100)#100픽셀만큼 전진
park.shape("circle")#펜모양은 원
park.forward(-100)#100픽셀만큼 후진
park.right(90)   #오른쪽으로 90도 회전
park.forward(-20)#20픽셀만큼 전진
park.left(90)       #왼쪽으로 90도 회전
park.forward(-100)  #100픽셀만큼 후진

#13장 연습문제 4번
import turtle       #터틀모듈을 불러온다
class MyTurtle(turtle.Turtle): #MyTurtle을 나타내는 클래스 정의
    def drawSquare(self):       #drawSquare정의
        for i in range(4):      #4번 반복
            self.right(90)      #오른쪽으로 90도 회전
            self.forward(100)   #100픽셀만큼 전진   
my_turtle = MyTurtle()      #클래스를 이용해 생성
my_turtle.forward(100)      #100픽셀만큼 전진
my_turtle.drawSquare()      #drawSquare 사용