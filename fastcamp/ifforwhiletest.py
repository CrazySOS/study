# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 못푼 문제 : 1,

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요. ########
from re import L


q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for a in q1.keys():
    if  a == "가을":
        print(q1[a])
    else:
        pass

for a1, a2 in q1.items():
    if a1 == "가을":
        print(a2)
        
# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for b, c in q2.items():
    if b or c == "사과":
        print("사과가 포함되어 있습니다.")
        break
else:
    print("사과가 없습니다.")
# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
q3 =  77

if 81 <= q3 <= 100: 
    print("A학점")
elif 61 <= q3 <= 80:
    print("B학점")
elif 41 <= q3 <= 60:
    print("C학점")
elif 21 <= q3 <= 40:
    print("D학점")
elif 0 <= q3 <= 20:
    print("E학점")
else:
    print("점수 정보가 없습니다.")

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
q4 = [12, 6, 18]
print(len(q4))
q41 = q4[0]
q42 = q4[1]
q43 = q4[2]
if q41 > q42 and q41 > q43:
    print(q41)
elif q42 > q41 and q42 > q43:
    print(q42)
elif q43 > q41 and q43 > q42:
    print(q43)
# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
o = '891022-4473837'
print(len(o))
print(o[7])

if int(o[7]) == 1 or int(o[7]) == 3:
    print("남자")
elif int(o[7]) == 2 or int(o[7]) == 4:
    print("여자")
else:
    print("주민등록번호 오류")
# 6 ~ 10 반복문 사용(while 또는 for)
# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q6 = ["갑", "을", "병", "정"]
for n in q6:
    if n == "정":
        continue
    print(n)

q6_1 = [t for t in q6 if t != "정"]
print(q6_1)
# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for w in range(1, 101):
    nums = w % 2
    if nums != 0:
        print(w, end=" ")

print("\n")

q7 = [i for i in range(1, 101) if i % 2 != 0]
print(q7)
# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q8 = ["nice", "study", "python", "anaconda", "!"]
for g in q8:
    if len(g) >= 5:
        print(g)

q8_1 = [z for z in q8 if len(z) >= 5]
print(q8_1)
# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q9 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for j in q9:
    if j.islower():
        print(j)

q9_1 = [k for k in q9 if k.islower()]
print(q9_1)
# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q0 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for m in q0:
    if m.isupper():
        print(m.lower())
    else:
        print(m.upper())

# 리스트 컴프리헨션(list comperhension)
number = []

for v in range(1, 101):
    number.append(v)
print(number, end = "")


num = [x for x in range(1, 101)]
print(num, end = "")














