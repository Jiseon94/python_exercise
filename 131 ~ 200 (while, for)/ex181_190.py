#181
apart =[]
# apart.append(("101호", "102호"))
# apart.append(("201호", "202호"))
# apart.append(("301호", "302호"))
apart.append(["101호", "102호"])
apart.append(["201호", "202호"])
apart.append(["301호", "302호"])
print(apart)


#182
stock = [['시가',100,200,300],['종가', 80,210,330]]
print(stock)

#183
stock = {'시가':[100,200,300], '종가':[80,210, 330]}
print(stock)

#184
stock = {"10/10":[80,110,70,90], "10/11":[210,230, 190, 200]}
print(stock)

#185
apart = [ [101, 102], [201, 202], [301, 302] ]
# print(apart[0][0],"호")
# print(apart[0][1],"호")
# print(apart[1][0],"호")
# print(apart[1][1],"호")
# print(apart[2][0],"호")
# print(apart[2][1],"호")

for row in apart:
    print(row)
    for col in row:
        print(col, "호")

print("=====================")
#186
for row in apart[::-1]:
    print(row)
    for col in row:
        print(col, "호")

print("=====================")

#187
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart[::-1]:
    # print(row)
    for col in row[::-1]:
        print(col, "호")

#188
for row in apart:
    for col in row:
        print(col,"호")
        print("----")

#189
for row in apart:
    for col in row:
        print(col,"호")

    print("----")

#190
for row in apart:
    for col in row:
        print(col,"호")
print("----")


