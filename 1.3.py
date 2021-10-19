total =100000       #총 재료비용
americano_price = 2000
cafelatte_price = 3000
capucino_price = 3500

americanos = int(input("아메리카노 판매 개수:"))
cafelattes = int(input("카페라테 판매 개수:"))
capucinos = int(input("카푸치노 판매 개수:"))

sales = americanos*americano_price
sales = sales + cafelattes*cafelatte_price
sales = sales + capucinos*capucino_price
print("총 매출은 , "sales,"입니다.")

if (total<sales) : print("흑자입니다.")
else : print("적자입니다.")


ctemp = int(input(?"섭씨온도: "))
ftemp = 9/5*ctemp+32
print("화씨온도:",ftemp)


money = int(input("투입한 돈: "))
price = int(input("물건 값:"))

change = money-price
print("거스름돈:", change)
coin500s = change//500              #500으로 나누어서 몫이 500원 짜리의 개수
change = change % 500               #500으로 나눈 나머지를 계산
coin100s = change//100              #100으로 나누어서 몫이 500원 짜리의 개수
change = change % 100               #100으로 나눈 나머지를 계산
coin50s = coin//50                  #50으로 나누어서 몫이 500원 짜리의 개수
change = change % 50                #50으로 나눈 나머지를 계산
coin10s = coin//10                  #10으로 나누어서 몫이 500원 짜리의 개수
change = change % 10                #10으로 나눈 나머지를 계산
print("500원 종전의 개수:",coin500s)
print("100원 종전의 개수:",coin100s)
print("50원 종전의 개수:",coin50s)
print("10원 종전의 개수:",coin10s)


money = int(input("투입한 돈:"))    #변수 money를 선언하고 정수형으로 받는다
price = int(input("물건값:"))       #변수 price를 선언하고 정수로 받는다

change = money-price               #거스릅돈을 계산한다
coin500s = change//500             #500으로 나누어서 몫이 500원 짜리의 개수이다
change = change % 500              #500으로 나눈 나머지를 계산
coin100s = change//100             #100으로 나누어서 몫이 100원 짜리의 개수이다

print("500원 종전의 개수:",coin500s)    #거슬러줄 500원 짜리의 개수를 출력한다.
print("100원 종전의 개수:",coin100s)    #거슬러줄 100원 짜리의 개수를 출력한다.