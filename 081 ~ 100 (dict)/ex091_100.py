#91
inventory = {"메로나":[300, 20], "비비빅":[400,3], "죠스바":[250,100]}
print(inventory, type(inventory))

#92
print(inventory["메로나"][0], "원")

#93
print(inventory["메로나"][1], "개")

#94
inventory["월드콘"] = [500, 7]
print(inventory)

#95
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# list = icecream.keys()
# print(list, type(list))
ice = list(icecream.keys())
print(ice, type(ice))

#96
val = list(icecream.values())
print(val, type(val))

#97
print(sum(val))

#98
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

#99
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

result = {}
zipped = zip(keys, vals)
# print(zipped, type(zipped))
zipped = dict(zipped)
print(zipped, type(zipped))

#100
date = ['09/05', '09/06', '09/07', '09/08', '09/09', "09/10"]
close_price = [10500, 10300, 10100, 10800, 11000, 12000]

close_table =dict(zip(date,close_price))
print(close_table,type(close_table))
