#011
#삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
삼성전자 = 50000
print(삼성전자 * 10)

#012
#다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요. (문제가 이해가 안된다...)
#항목	    값
# 시가총액	298조
# 현재가	50,000원
# PER	    15.79
시가총액 = "298조"
현재가 = 50000
per = 15.79
print(per)

시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

#13
# 변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.
#
# >> s = "hello"
# >> t = "python"
# 두 변수를 이용하여 아래와 같이 출력해보세요.
#
# 실행 예:
# hello! python

s = "hello"
t = "python"
print(s+"!",t)

#14
# 아래 코드의 실행 결과를 예상해보세요.
#
# >> 2 + 2 * 3

#답 : 8

#15
# type() 함수는 데이터 타입을 판별합니다. 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.
# 아래 변수에 바인딩된 값의 타입을 판별해보세요.
#
# >> a = "132"
a="132"
print(type(a))  #<class 'str'>

#16
# 문자열 '720'를 정수형으로 변환해보세요.
#
# >> num_str = "720"

num_str = "720"
print(num_str, type(num_str))
num_int = int(num_str)
print(num_int,type(num_int))
print(num_int+1, type(num_int))

#17
num=100
str = str(num)
print(str, type(str))

#18
a="15.79"
f=float(a)
print(f, type(f))

#19
year = "2020"
int = int(year)
print(int+3)
print(int+2)
print(int+1)

#20
a=48584
b=36
print(a*b)
