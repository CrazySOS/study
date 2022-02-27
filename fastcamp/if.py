# 패스트캠퍼스 if 

a = []

if a:
    print("True")
else:
    print("False")

b = 100
c = 60
d = 15

print(b > c and c > d)
print(b > c or d > c)
print(not b > c)

# 산술 > 관계 > 논리 순서로 적용됨

print(5+10 > 0 and not 7 + 3 == 10)

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print("합격하셨습니다.")
else:
    print("불합격입니다.")


# 다중조건문

num = 90

if num >= 90:
    print("num 등급 A", num)
elif num >= 80:
    print("num 등급 B", num)
elif num >= 70:
    print("num 등급 C", num)
else:
    print("꽝")


# 중첩 조건문

age = 27
height = 175

if age >= 20:
    if height >= 170:
        print("A 지망 지원가능")
    elif height >= 160:
        print("B 지망 지원가능")
    else:
        print("지원불가")
else:
    print("20세이상 지원가능")
















