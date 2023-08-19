#31
#34

#32
#HiHiHi

#33
print("-"*80)

#34
t1 = 'python'
t2 = 'java'
r = t1+" "+t2+" "
print(r*4)

#35
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13

print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

#36
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

#37
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

#38
상장주식수 = "5,969,782,550"
r=상장주식수.replace(",","")
result = int(r)
print(result, type(result))

#39
분기 = "2020/03(E) (IFRS연결)"
print(분기[0:7])

#40
data = "   삼성전자    "
result = data.strip()
print(result)