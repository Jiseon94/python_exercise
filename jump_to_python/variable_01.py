a=[1,2,3]
b=a
a[1]=4
print(a)
print(b)

print(id(a))    #3191205873344
print(id(b))    #3191205873344

print(a is b) #True

#a의 주소값이 아니라, 변수값만 넘기고 싶다면? 복사의 개념!
b=a[:]
print(b)
print(id(b))    #2789029696000
print(a is b)   #False


