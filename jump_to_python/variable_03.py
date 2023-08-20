# a= 1
# b=2
# print(a)
# print(b)
# tmp = b
# b = a
# a= tmp
# print(a)
# print(b)
# print(tmp)

#더 간단한 방법이 있다.
a=1
b=2
a, b = b, a
print(a)    #2
print(b)    #1
print(a,b)

x=(1,2,3)
print(id(x))    #2724330764096
x=x+(4,)
print(x)
print(id(x))    #2724330793024
#착각하지 말기. 튜플은 수정 불가능하다.
#튜플에 값을 추가한것처럼 보이지만, 실제로는 새롭게 튜플을 만들어 놓은걸