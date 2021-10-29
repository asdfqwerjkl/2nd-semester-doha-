#탄화수소의 종류를 알아내는 코드를 만들어 볼것이다.

arcane = int(input("당신이 아는 탄화수소의 탄소수는 몇개인가요?:"))
x = (input("혹시 당신의 탄화수소에 하이드록시기가 붙나요?(yes/no):"))
if arcane == 1 and x == 'yes' : 
    print("당신의 탄화수소는 메테인이군요!")
elif arcane == 1 and x == 'no' : 
    print("당신의 탄화수소는 메탄올이군요!")
elif arcane == 2 and x == 'yes': 
    print("당신의 탄화수소는 에테인이군요!")
elif arcane == 2 and x == 'no': 
    print("당신의 탄화수소는 에탄올이군요!")
elif arcane == 3 and x == 'yes': 
    print("당신의 탄화수소는 프로페인이군요!")
elif arcane == 3 and x == 'no': 
    print("당신의 탄화수소는 프로판올이군요!")
elif arcane == 4 and x == 'yes': 
    print("당신의 탄화수소는 뷰테인이군요!")
elif arcane == 4 and x == 'no': 
    print("당신의 탄화수소는 뷰탄올이군요!")
elif arcane == 5 and x == 'yes': 
    print("당신의 탄화수소는 펜테인이군요!")
elif arcane == 5 and x == 'no': 
    print("당신의 탄화수소는 펜탄올이군요!")
elif arcane == 6 and x == 'yes': 
    print("당신의 탄화수소는 헥세인이군요!")
elif arcane == 6 and x == 'no': 
    print("당신의 탄화수소는 헥산올이군요!")
elif arcane == 7  and x == 'yes': 
    print("당신의 탄화수소는 헵테인이군요!")
elif arcane == 7  and x == 'no': 
    print("당신의 탄화수소는 헵탄올이군요!")
elif arcane == 8 and x == 'yes': 
    print("당신의 탄화수소는 옥테인이군요!")
elif arcane == 8 and x == 'no': 
    print("당신의 탄화수소는 옥탄올이군요!")
elif arcane == 9 and x == 'yes': 
    print("당신의 탄화수소는 노네인이군요!")
elif arcane == 9 and x == 'no': 
    print("당신의 탄화수소는 노난올이군요!")
elif arcane == 10 and x == 'yes': 
    print("당신의 탄화수소는 데케인이군요!")
elif arcane == 10 and x == 'no': 
    print("당신의 탄화수소는 데칸올이군요!")
