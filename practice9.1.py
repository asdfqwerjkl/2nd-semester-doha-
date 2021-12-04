list = []
sum = 0 
for i in range(5):  
    num = int(input("정수를 입력하시오:"))
    list.append(num)
for a in range(5): 
    sum = sum+list[a] 
print(sum/len(list))    