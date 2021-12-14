#11장 연습문제 1번
filename = input("파일 이름을 입력하세요: ").strip() #변수입력
infile = open(filename, "r") 
count = 0       #count 생성
for line in infile:     #글자의 개수 세기
    for ch in line:
        count += 1
print("파일 안에는 총 ", count , "개의 글자가 있습니다.") #출력
infile.close() # 파일을 닫는다

#11장 연습문제 2번
infilename = input("파일 이름을 입력하시오: ").strip()  #변수입력
infile = open(infilename, "r")      #파일열기,읽기모드
file_s = infile.read() 
removed_s = input("삭제할 문자열을 입력하시오: ").strip()#변수입력
modified_s = file_s.replace(removed_s, "")
infile.close()                      #파일닫기
outfile = open(infilename, "w")     #파일열기,쓰기모드
print(modified_s, file = outfile, end = "") #출력
print("변경된 파일이 저장되었습니다.") 
outfile.close()                     #파일닫기

#11장 연습문제 3번
infile = open(filename, "r")    #읽기모드,파일열기
for line in infile:
    ...
def countLine(line, counter):       #contline정의
    for ch in line:
        if ch.isalpha():
            if ch in counter:
                counter[ch] = counter[ch] + 1
            else:
                counter[ch] = 1
fname = input("입력 파일 이름: ").strip()
infile = open(fname, "r")       #읽기모드,파일열기
my_dict = { }           #변수생성
for line in infile:
        countLine(line, my_dict)
print(my_dict)          #my_dict출력
infile.close()      #파일을 닫는다