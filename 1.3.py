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
coin500s = change//500
change = change % 500
coin100s = change//100
change = change % 100
coin50s = coin//50
change = change % 50
coin10s = coin//10
change = change % 10
print("500원 종전의 개수:",coin500s)
print("100원 종전의 개수:",coin100s)
print("50원 종전의 개수:",coin50s)
print("10원 종전의 개수:",coin10s)


money = int(input("투입한 돈:"))
price = int(input("물건값:"))

change = money-price
coin500s = change//500
change = change % 500
coin100s = change//100

print("500원 종전의 개수:",coin500s)
print("100원 종전의 개수:",coin100s)