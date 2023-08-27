#191
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for row in data:
    # print(i)
    for col in row:
        print(col*1.00014)
    print("-"*5)


#192

#193
result = []
for row in data:
    # print(i)
    for col in row:
        print(col*1.00014)
        result.append(col*1.00014)
print(result)

print("=============")
#194
result = []
for line in data:
    sub = []
    for column in line:
        # print(col*1.00014)
        sub.append(column*1.00014)
        # print(sub)
    result.append(sub)
print(result)
print("=============")
result = []
for line in data:
    sub = []
    for column in line:
        sub.append(column * 1.00014)
    result.append(sub)
print(result)

#195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
# print(ohlc[1][3])
# print(ohlc[2][3])
# print(ohlc[3][3])
for i in ohlc[1::]:
    # print(i)
    print(i[3])

#196
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in ohlc[1::]:
    if i[3]>150 :
        print(i[3])

print("=========")
#197
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1::]:
    if i[3]>=i[0]:
        print(i[3])

#198
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
volatility = []
for i in ohlc[1::]:
    volatility.append(i[1]-i[2])
print(volatility)

#199
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in ohlc[1::]:
    if i[3]>i[0]:
        print(i[1]-i[2])

#200
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
sum = 0
for i in ohlc[1::]:
    sum+=(i[3]-i[0])
print(sum)
