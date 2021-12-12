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
