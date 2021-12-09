#9장 연습문제 7번
domains = {"kr":"대한민국","sk":"슬로바키아","no":"노르웨이","us":"미국","jp":"일본","hu":"헝가리","de":"독일"}
for k,v in domains.iems():
    print(k,":",v)

domains = {"kr":"대한민국","sk":"슬로바키아","no":"노르웨이","us":"미국","jp":"일본","hu":"헝가리","de":"독일"}
for key i ndomains.key():
    print(key,":",domains[key])

#9장 연습문제 8번
problems = {'파이썬':'최근에 가장 떠오르는 프로그래밍 언어'
    '변수':'데이터를 저장하는 메모리 공간',
    '함수':'작업을 수행하는 문장들의 집합에 이름을 붙인것',
    '리스트':'서로 관련이 없는 항복들의 모임'}

for word in problems.key():
    print("다음은 어떤 단어에 대한 설명일까요?")
    print(problems[word])
    print("(1)파이썬(2)함수(3)리스트(4)변수")
    ans = input()

if ans == word:
    print("정답입니다.!")
else:
    print("정답이 아닙니다.!")