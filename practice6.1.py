#1번 연습문제
for i in range(2,102,2): 
    print(i,end=" ")
    
#2번 연습문제    
year = 0
balance = 1000 
while balance <= 2000: 
    year = year+1 
    interest = balance*0.07 
    balance = balance + interest
print(year,"년이 걸립니다.")

#3번 연습문제
print(" 첫번째 sum의 값은 4, 두번째 sum의 값은 7, 세번째 sum의 값은 9, 네번째 sum의 값은 10이 나온다.")

#4번 연습문제
x = 0
while x <= 26 or x >= 28 : 
    x = int(input("3*9는"))
print("맞았습니다.")

#5번 연습문제
sum = 0 
x = 0
while True: 
    x = int(input("정수를 입력하시오:"))
    sum = sum + x
    if x == 0:
        break;
print("합은",sum,"입니다.")

#6번 연습문제
import random
number1= random.randint(1,6)
number2= random.randint(1,6)
print("첫번째 주사위=",number1,"두번째 주사위=",number2)
