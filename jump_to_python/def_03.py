#Lambda
# 함수를 간단하게 표현하는 방법.
# def add(a,b):
#     return a+b


add = lambda a, b: a+b
print(add(1,2))

myList = [lambda a, b: a+b, lambda a, b:a*b]

print(myList[1](1,2))   #2
