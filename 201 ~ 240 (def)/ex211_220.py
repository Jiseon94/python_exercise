#211
#안녕
#Hi

#212
#7
#15

#213
#함수() 매개변수를 문자열을 넣어야 실행되는데, 빈 괄호라서 에러.

#214
#서로 다른 타입의 파라미터라서 + 가 적용되지 않는다.

#215
def print_with_smile(string):
    print(string+":D")

print_with_smile("hi")

#216
print_with_smile("안녕하세요")

#217
def print_upper_price(price):
    # print(price+(price*0.3))
    print(price*1.3)

print_upper_price(100)

#218
def print_sum(a, b):
    print(a+b)

print_sum(3, 5)

#219
def print_arithmetic_operation(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)

print_arithmetic_operation(4, 2)

#220
def print_max(a, b, c):
    # print(max(a,b,c))
    if a> b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    else:
        print(c)

print_max(48,548,52)