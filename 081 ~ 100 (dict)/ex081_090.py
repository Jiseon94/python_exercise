#81
a, b, *c = (0, 1, 2, 3, 4, 5)
print(c)

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
print(len(scores))
*valid_score, _,_ = scores
print(valid_score)

print(len(valid_score))

#82
_, _, * valid_score = scores
print(valid_score)

#83
_, *valid_score, _ = scores
print(valid_score)

#84
temp = {}
print(temp, type(temp))

#85
pdt={'메로나':1000, '폴라포':1200, '빵빠레':1800}
print(pdt, type(pdt))

#86
pdt['죠스바'] = 1200
pdt["월드콘"] = 1500
print(pdt, type(pdt))

#87
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print("메로나 가격:", ice.get("메로나"))
print("메로나 가격:", ice["메로나"])

#88
ice["메로나"] = 1300
print(ice)

#89
del ice["메로나"]
print(ice)

#90
# ice["누가바"]
