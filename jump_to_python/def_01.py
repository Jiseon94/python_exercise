def sum(a, b):
    result = a+b
    return result
print(sum(1,2))

def say():
    return 'Hi'

print(say())

def sum(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

# sum(1,2)    #1, 2의 합은 3입니다.
print(sum(1,2)) #1, 2의 합은 3입니다.
                      #None


myList = [1,2,3]
print(myList.append(4)) #None. 추가만 했을뿐, return 값이 없어서 출력이 안되는거다.
print(myList)   #[1, 2, 3, 4]

print(myList.pop()) #4. pop함수에는 return 값이 있기에 마지막 숫자가 출력되는거다.
print(myList)   #[1, 2, 3]

def sum_many(*args):
    sum=0
    for i in args:
        sum = sum+i
    return sum
print(sum_many(1,2,3,4,100))    #110

def print_kwargs(**kwargs):
    for k in kwargs.keys():
        if(k == "name"):
            print("당신의 이름은: "+kwargs[k])

print(print_kwargs(name="int 조수", b="2"))