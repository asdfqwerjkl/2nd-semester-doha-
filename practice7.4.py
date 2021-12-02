#7장 연습문제
PI =3.14
def circleArea(radius): 
    return PI*(radius**2)
def circleCircumference(radius): 
    return PI*radius*2

print("반지름이 5인 원의 면적:",circleArea(5))
print("반지름이 5인 원의 둘레 :",circleCircumference(5))

#8장 연습문제 
a = 20
b = 10
def add(a,b): 
    return a+b 
sum = add(a,b) 
print("("+str(a)+"+"+str(b)+")"+"=",sum)

def add(a,b): 
    return a*b 
x = add(a,b) 
print("("+str(a)+"X"+str(b)+")"+"=",x)

def add(a,b): 
    return a/b 
y = add(a,b) 
print("("+str(a)+"/"+str(b)+")"+"=",y)
