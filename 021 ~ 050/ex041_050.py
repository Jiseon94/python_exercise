#41
ticker = "btc_krw"
re = ticker.upper()
print(re)

#42
ticker = "BTC_KRW"
re = ticker.lower()
print(re)

#43
a="hello"
b=a.capitalize()
print(b)

#44
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))

#45
file_name = "보고서.xlsx"
# print(file_name.endswith("xlsx | xls")) #False
print(file_name.endswith(("xlsx", "xls")))
print("=======================")

#46
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))

#47
a = "hello world"
# b= a.split(" ")
# print(b)
print(a.split())       #['hello', 'world']
print(a)               #hello world

#48
ticker = "btc_krw"
print(ticker.split("_"))

#49
date = "2020-05-01"
print(date.split("-"))

#50
data = "039490     "
data1 = data.rstrip()
print(data1)