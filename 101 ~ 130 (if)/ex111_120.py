#111
# user = input("입력:")
# print(user * 2)

#112, 113
# user = input("숫자를 입력하세요 : ")
# print(int(user)+10)
# if int(user)%2==0 :
#     print("짝수")
# else:
#     print("홀수")

#114
# if (int(user) +20) <= 255:
#     print(int(user)+20)
# else:
#     print("255")

#115
# num = int(user)-20
# if num<=0 :
#     print(0)
# elif num>=255:
#     print(255)
# else :
#     print(num)

#116
# time = input("현재시간:")
# if time[-2:] in "00":
#     print("정각 입니다.")
# else :
#     print("정각 아님")

#117
# fruit = ["사과", "포도", "홍시"]
# user = input("좋아하는 과일은? ")
# if user in fruit :
#     print("정답입니다.")
# else:
#     print("오답")

#118
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# user = input("종목명: ")
# if user in warn_investment_list:
#     print("투자 경고 종목")
# else:
#     print("경고 종목 아님")

#119
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# user = input("제가좋아하는 계절은 : ")
# if user in fruit.keys() :
#     print("정답")
# else:
#     print("오답")

#120
user = input("좋아하는 과일은? ")
if user in fruit.values():
    print("정답")
else:
    print("오답")
