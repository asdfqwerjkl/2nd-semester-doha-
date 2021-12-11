#자동차를 클래스로 선언하고 생성하면서 초기화도 하라
class Car: 
    def __init__(self,speed,color,model):
        self.speed = speed
        self.color = color
        self.model = model
    def __del__(self):
        print("인스턴스를 소멸시킵니다.")
    def show_info(self):
        print("이름:",self.model,"/색상:",self.color,"/속도:",self.speed)
car1 = Car("100km/h","푸른색","소나타")
car1.show_info()
del car1