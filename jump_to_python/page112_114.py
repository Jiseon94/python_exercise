#1
a=80
b=75
c=55
print((a+b+c)/3)

#2
print(13%2)

#3
pin="881120-1068234"
# yyyymmdd = pin[:6]
# print(yyyymmdd)
yyyymmdd = pin.split("-")
print(yyyymmdd[0])

num=yyyymmdd[1]
print(num)

#4
gen = pin[7]
print(gen)

#5
a="a:b:c:d"
b=a.replace(":", "#")
print(b)

#6
a=[1,3,5,4,2]
a.sort()
print(a)
a.reverse()
print(a)

#7
a=['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

#8
a=(1,2,3)
# a2=(4,)
a = a+(4,)
print(a)

#9
a= dict()
print(a)
a['name'] = 'python'
a[('a',)] = 'python'
# a[[1]] = 'python'
a[250] = 'python'
print(a)
