#21
letters='python'
print(letters[0], letters[2])

#23
s = "홀짝홀짝홀짝"
print(s[0]+ s[2]+ s[4])
print(s[::2])

#22
l = "24가 2210"
print(l[-4:])

#24
string = "PYTHON"
print(reversed(string)) #<reversed object at 0x0000013C23FEBA00>
r = "".join(reversed(string))
print(r)    #NOHTYP

print(string[::-1])

#25
phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))

#26
print(phone_number.replace("-", ""))

#27
url = "http://sharebook.kr"
print(url[-2::])        #kr

url_split = url.split('.')
print(url_split[-1])    #kr
print(url_split[0])     #http://sharebook

#28
#python

#29
string = 'abcdfe2a354a32a'
print(string.replace("a", "A"))

#30
#aBcd