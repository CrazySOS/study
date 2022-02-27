# 패스트캠퍼스 반복문 강의


v1 = 1
while v1 < 11:
    print(v1)
    v1 += 1

for v2 in range(10):
    print(v2)

for v3 in range(1,10):
    print(v3)


# 시퀀스(순서가 있는) 자료형 반복
# > 문자열, 리스트, 튜플, 집합, 사전
# 사용 함수(iterable) : range, reversed, enumerate, filter, map, zip

names = ["kim", "park", "cho", "choi", "yoo"]

for name in names:
    print("you are ", name)
    
word = "dreams"

for s in word:
    print("word is ", s)

my_info = {
    "name" : "Kim",
    "age" : 33,
    "city" : "seoul"
}

for key in my_info:
    print("my info is ", key)

for key in my_info.values():
    print("my info is ", key)

for key in my_info.keys():
    print("my info is" , key)

for k, v in my_info.items():
    print("my info is", k, v)


na = "KennRY"

for n in na:
    if n.isupper(): # n 이 대문자라면
        print(n.lower())
    else:
        print(n.upper())


# break (for문)

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 33:
        print("found : 33")
        break
    else:
        print("not found")


# for - else
for num in numbers:
    if num == 32:
        print("found : 32")
        break
    else:
        print("not found")
else:
    print("not found 32")


# continue

lt = ["1", 2, 5, True, 4.3, complex(4)]

for u in lt:
    if type(u) is float:
        print("found")
    
for u in lt:
    if type(u) is float:
        continue
    print("type", type(u))














