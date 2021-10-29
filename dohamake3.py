#mbti 검사 만드는 코딩
m = int(input("당신은 외향적인가요? 내향적인가요? \n 1.외향적이다. \n 2.내향적이다.:"))
b = int(input("당신은 실제경험을 중시하나요? 육감에 의존하나요?\n 1.실제 경험을 중시한다.\n 2.육감에 의존한다.:"))
t = int(input("당신은 객관적인가요? 감정적인가요?\n 1.객관적이다.\n 2.감정적이다.:"))
i = int(input("당신은 계획적인가요? 융통적인가요?\n 1.계획적이다.\n 2.융통적이다.:"))
if m == 1 and b == 1 and t == 1 and i == 1: 
    print("당신은 ESTJ(팩폭 잘하는 지휘관)입니다.")
elif m == 1 and b == 1 and t == 1 and i == 2: 
    print("당신은 ESTP(치고박는 행동파)입니다.")
elif m == 1 and b == 1 and t == 2 and i == 1: 
    print("당신은 ESFJ(철두철미)입니다.")
elif m == 1 and b == 1 and t == 2 and i == 2: 
    print("당신은 ESFP(분위기 메이커)입니다.")
elif m == 1 and b == 2 and t == 1 and i == 1: 
    print("당신은 ENTJ(전형적인 리더)입니다.")
elif m == 1 and b == 2 and t == 1 and i == 2: 
    print("당신은 ENTP(다재다능 팔방미인)입니다.")
elif m == 1 and b == 2 and t == 2 and i == 1: 
    print("당신은 ENFJ(강강약약)입니다.")
elif m == 1 and b == 2 and t == 2 and i == 2: 
    print("당신은 ENFP(호기심 지옥)입니다.")
elif m == 2 and b == 1 and t == 1 and i == 1: 
    print("당신은 ISTJ(원리원칙 주의)입니다.")
elif m == 2 and b == 1 and t == 1 and i == 2: 
    print("당신은 ISTP(독고다이 달인)입니다.")
elif m == 2 and b == 1 and t == 2 and i == 1: 
    print("당신은 ISFJ(독특한 원칙주의자)입니다.")
elif m == 2 and b == 1 and t == 2 and i == 2: 
    print("당신은 ISFP(성인군자)입니다.")
elif m == 2 and b == 2 and t == 1 and i == 1: 
    print("당신은 INTJ(차가운 인간)입니다.")
elif m == 2 and b == 2 and t == 1 and i == 2: 
    print("당신은 INTP(따뜻한 로봇)입니다.")
elif m == 2 and b == 2 and t == 2 and i == 1: 
    print("당신은 INFJ(낭만주의자)입니다.")
elif m == 2 and b == 2 and t == 2 and i == 2: 
    print("당신은 INFP(세상감성적)입니다.")
    
q = input("혹시 제 mbti가 궁금하시나요?(y/n):")
if q == 'y' :  
    print("저의 mbti는 ENFJ(강강약약)입니다.\n이상으로 mbti 검사를 마치겠습니다.")
elif q == 'n': 
    print("이상으로 mbti 검사를 마치겠습니다.")