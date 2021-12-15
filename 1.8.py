import random           #랜덤모듈을 불러온다.
question = ["56 / 8", "8 * 9", "50 - 25", "1 + 6", "81 / 9",
 "22 + 10", "8 / 4", "9 * 7", "17 - 4", "3 + 5"]
dailyQuestion = random.choice(question)     #dailyQuestion변수의 숫자 
print("#########################")          #출력
print("# 오늘의 산수 문제 #")                #출력
print("#########################")          #출력
print("")                                   #출력
print(dailyQuestion)                        #출력


items = {"커피음료": 7, "펜": 3, "종이컵": 2, "우유": 1, "콜라": 4, "책": 5}
while True:     #반복문
    print("")   #출력
    print("# 재고 목록 #")              #출력
    for key in sorted(items.keys()):   #반복문     
    print(key, items[key])              #출력
    print("\n********************")     #출력
    print("0. 종료")                    #출력
    print("1. 재고 추가")               #출력
    print("2. 재고 삭제")               #출력
    print("********************\n")     #출력
    a = int(input("무엇을 하시겠습니까?: "))    #a의 변수 입력
 
    if a == 1:                      #가정문
        item = input("물건의 이름을 입력하시오: ")      #item의 변수 입력
        num = input("몇개를 추가하시겠습니까? :")       #num의 변수 입력
        items[item] = int(items[item]) + int(num)     
    elif a == 2:                    #가정문
        item = input("물건의 이름을 입력하시오: ")       #item의 변수 입력
        num = input("몇개를 삭제하시겠습니까? :")       #num의 변수 입력
        items[item] = int(items[item]) - int(num)
 
    else:                   #가정문
        break               #루프밖으로 분기

english_dict = dict()           #사전식
english_dict['하나'] = 'one'            #하나면 one
english_dict['둘'] = 'two'              #둘이면 two
english_dict['셋'] = 'three'            #셋이면 three
word = input("단어를 입력하시오: ")     #입력
print (english_dict[word])          #출력

import smtplib              #SMTP을 사용하기 위한 모듈
from email.mime.text import MIMEText    #메일을 보낼때 메시지의 제목과 본문을 설정하기 위한 모듈
me = 'abc@server.kr' # 보내는 사람 메일 주소
you = ['def1@server.com','def2@server.com','def3@server.com'] # 받는 사람 메일 주소
contents = '12월 20일에 동창회가 있으니 참석해주시기 바랍니다.'     #contents변수
msg = MIMEText(contents, _charset='euc-kr')         
msg['Subject'] = '동창회 모임'  #메일의 제못을 지정해준다
msg['From'] = me                #보내는 사람을 지정해준다
msg['To'] = you                 #받는 사람을 지정해준다
server = smtplib.SMTP('smtp.gmail.com', 587)    #지메일의 포트 번호  = 587
server.ehlo()               #SMTP서버에 메시지를 보내주는 메소드
server.starttls()           #TLS보안 시작
server.ehlo()
server.login("자신의 아이디", "패스워드")   #로그인을 인증(지메일계정, 앱 비밀번호)
for i in range(len(you)):           #반복문
    server.sendmail(me, you[i], msg.as_string())
server.quit()       #STMP서어봐의 연결종료