# a = input()
#input은 내장 함수로써, 입력을 받는 함수이다.
# print(a)

# number = input("숫자 입력하시오: ")
# print(number)

f = open("새파일.txt", "w", encoding="UTF-8")
for i in range(1,11):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close()

#파일 읽어보기 (한줄)
f = open("새파일.txt", "r", encoding="UTF-8")
line = f.readlines()
print(line)
f.close()   #파일을 오픈했으면 무조건 클로즈를 해줘야한다! 이걸 안닫아두면 문제가 생길 수 있다

#여러줄 읽어보기
f = open("새파일.txt", "r", encoding="UTF-8")
while True :
    line = f.readlines()
    if not line: break
    print(line)
f.close()