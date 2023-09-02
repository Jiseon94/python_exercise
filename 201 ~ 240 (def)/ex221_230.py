#221
def print_reverse(a):
    # a = reversed(a)
    print(a[::-1])
print_reverse("python")

#222
def print_score(list):
    print(sum(list)/len(list))

print_score([1,2,3])

#223
def print_even (even_list):
    for i in even_list:
        if i%2 ==0:
            print(i)

print_even([1, 3,5,6])

#224
def print_keys(dict):
    for keys in dict.keys():
        print(keys)

print_keys ({"이름":"김말똥", "나이":30, "성별":0})

#225
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
print("테스트:", my_dict.keys())
print("테스트:", my_dict.get("10/26"))
print("테스트:", my_dict["10/26"])

def print_value_by_key(my_dict, date):
    print(my_dict.get(date))

print_value_by_key(my_dict, "10/26")

def print_value_by_key(my_dict, date):
    print(my_dict[date])

print_value_by_key(my_dict, "10/26")

#226
def print_5xn(string):
    print(string[0:5])
    print(string[5:11])

print_5xn("아이엠어보이유알어걸")
#하지만 이렇게 하면 재사용성이 없음...

def print_5xn(line):
    chunk_num = int(len(line)/5)
    for x in range(chunk_num+1):    #5로 나누고 나머지가 있을테니 +1을 하는거임.
        print(line[x*5:x*5+5])

print_5xn("아이엠어보이유알어걸")

#227
def print_mxn(string, int):
    print(string)

# printmxn("아이엠어보이유알어걸", 3)