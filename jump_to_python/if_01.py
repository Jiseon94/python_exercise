# money = 2000
# if 1  in [1,2,3] :
#     pass
# elif money:
#     print("hi")
# else:
#     print("걸어라")

score = 70
if score >= 60:
    message = "success"

else:
    message = "failure"
print(message)

message = "success" if score >=60 else "failure"
print(message)


treeHit= 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

test_list = ['one', 'two', 'three']
for i in test_list :
    print("있어요")

marks = [90, 25, 60, 70, 80]
number = 0
for mark in marks:
    number = number +1
    if mark >= 60:
        print("%d번 학생은 합격" %number)
    else:
        print("%d번 학생은 불합격" %number)

sum = 0
for i in range(1,11) :
    sum = sum +i
print(i)