#121
# user = input()
# print(user.islower()) #소문자:True, 대문자:False
# if user.islower():
#     print(user.upper())
# else:
#     print(user.lower())

#122
# score = int(input("score: "))
# if score <=100 and score >=81:
#     print("grade is A")
# elif score <=80 and score >=61:
#     print("grade is B")
# elif score <= 60 and score >= 41:
#     print("grade is C")
# elif score <=40 and score >=21:
#     print("grade is D")
# elif score <=20 and score >=0:
#     print("grade is E")

#123
# user = input("입력: ")
#
# if user[-2:] in "달러" :
#     print(int(user[:3])*1167, "원")
# elif user[-1:] in "엔" :
#     print(int(user[:4])*1.096, "원")
# elif user[-2:] in "유로" :
#     print(int(user[:2])*1268, "원")
# elif user[-2:] in "위안" :
#     print(int(user[:3])*171, "원")
#
# else :
#     print("변환불가")

#124
# num1 = input("num1: ")
# num2 = input("num2: ")
# num3 = input("num3: ")
#
# max = max(num1, num2, num3)
# print(max, type(max))

#125
# user = input("휴대전화 번호 입력 : ")
# user.split("-")
# 통신사 = {"011":"SKT", "016":"KT", "019": "LGU", "010":"알수없음"}
# if user.split("-")[0] in 통신사 :
#     print("당신은 %s 사용자입니다." %통신사[user.split("-")[0]])
# else :
#     print("알수없는")

#126
# user = input("우편번호 : ")
# num = int(user[2:3])
# if num in (0, 1, 2) :
#     print("강북구")
# elif num in (3,4,5) :
#     print("도봉구")
# elif num in (6,7,8,9) :
#     print("노원구")

#127
user = input("주민번호 : ")
# num = int(user.split("-")[1][0])
# if num in (2, 4) :
#     print("여자")
# elif num in (1,3):
#     print("남자")
# else:
#     print("뉘기야")

#128
# num = int(user.split("-")[1][1:3])
# if 0<= num <= 8:
#     print("서울")
# else:
#     print("서울아님")

#129
# num1 = user.split("-")
num1 = list("".join(user))
# print(num1,type(num1))
num1.remove("-")
print(num1,type(num1))
num2 = [2,3,4,5,6,7,8,9,2,3,4,5]
print(num2,type(num2))

# sum ={(num1) : (num2)}
# print(sum)

#130
# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
