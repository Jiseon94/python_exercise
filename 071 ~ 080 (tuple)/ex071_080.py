#71
my_variable = ()
print(my_variable, type(my_variable))

#72
movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
print(movie_rank)

#73
num = (1)
print(num, type(num))
num = (1,)
print(num, type(num))

#74
#튜플은 값을 변경할 수 없다.

#75
t = 1, 2, 3, 4
print(type(t))

#76
t = ('a', 'b', 'c')
t =  ('A', 'b', 'c')
print(t, type(t))

#77
interest = ('삼성전자', 'LG전자', 'SK Hynix')
# interest = [interest]
interest = list(interest)
print(interest, type(interest))

#78
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = tuple(interest)
print(interest, type(interest))

#79
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

#80
data = tuple(range(2, 100, 2))
print(data)