a = 1
def vartest(a):
    a = a+1     #return 값이 없기에 유효하지가 않다.

vartest(a)          #1
print(a)            #1
# print(vartest(a))  #none 이 나옴.

#전역변수에게 영향을 주고 싶다면? 2가지 방법이 있음
a = 1
def vartest(a):
    a = a+1
    return a

a = vartest(a)
print(a)

#2번째 방법. global 예약어를 쓴다.

a = 1
def vartest():
    global a    #전체에서 사용할 수 있는 변수라는 선언이 된다.
    a = a+1

vartest()   #return 값은 없지만, 위의 a=1 에 영향을 주게된다.
print(a)    #2