# 구구단

# n = int(input("구구단 몇단이 필요합니까? : ")) # 속성이 숫자임을 표기
# for m in range(1, 10):
#     m = int(m) # 속성이 숫자임을 표기
#     print(n, "x", m, "=" , n*m)

result = 0
for s in range(1, 1000):
    if s % 3 == 0 or s % 5 == 0:
        result += s
print(result)

def Totalp(z, x):
    if z % x == 0:
        return z // x + 1
    else:
        return z // x + 1

print(Totalp(5, 10))
print(Totalp(10, 10))
print(Totalp(15, 10))
print(Totalp(25, 10))

import os

def search(dirname):
    file = os.listdir(dirname)
    for name in file:
        fullname = os.path.join(dirname, name)
        if os.path.isdir(fullname):
            search(fullname)
        else:
            ext = os.path.splitext(fullname)[-1]
            if ext == ".py":
                print(fullname)

search("/Users/youngsoonsong/Desktop/study/")





