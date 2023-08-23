#161
for i in range(0,100):
    print(i)

#162
for i in range(2002,2051,4):
    print(i)

#163
for i in range(1,31):
    if i%3==0 :
        print(i)

#164
for i in range(100):
    print(99 - i)

#165
for i in range(0,10):
    print(float(i)/10)

#166
for i in range(1,10):
    print("3x{} = ".format(i),3*i)
    # print("3x",i, " = ", 3 * i)

#167
for i in range(1,10,2):
    print("3x{} = ".format(i),3*i)

#168
sum=0
for i in range(1,11):
    # sum = sum+i
    sum+=i

print("합:",sum)

#169
sum=0
for i in range(1,11,2):
    sum+=i
print(sum)

#170
num=1
for i in range(1,11):
    num*=i

print(num)