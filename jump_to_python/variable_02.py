#주소값 말고 값 자체를 복사시키는 다른 방법
from copy import copy

a=[1,2,3]
b=copy(a)
a[1]=4
print(a)    #[1, 4, 3]
print(b)    #[1, 2, 3]

print(id(a))    #2670814426496
print(id(b))    #2670814271488

print(a is b) #False
