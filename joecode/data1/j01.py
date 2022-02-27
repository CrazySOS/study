# 자료형

# a = 3 이라는 것은 3(오른쪽의 값)이라는 숫자를 a(왼쪽의 값)라는 박스에 담는다는 내용으로 쓴다.


from itertools import count
from unicodedata import name


a = "1234567890"

print(a[:6:2])

#리스트

a = ['송영순', '정인혁', '오인재', '사마은혁', ['지은수', '유해현']]
b = [1, 2, 3, 4, 5]
print(a[2]) #리스트의 지정값 불러오기
print(a[4][1]) #리스트안에있는 리스트의 지정값 불러오기
print(b[2]+b[3]) #숫자형 리스트의 값끼리의 연산도 가능
print(a+b) #리스트 합쳐서 출력하기
print(b * 3) #반복 출력

a[1] = '유나래'
print(a)
b[0:2] = 0, 100
print(b)
b[1:3] = [ ]
print(b)
del a[4]
print(a)
a.append('주우민')
print(a)
a.sort()
print(a)
b.reverse()
print(b)
print(a.index('송영순'))
b.insert(0, 0)
print(b)
b.remove(5)
print(b)
print(a.pop())
print(a)
print(b.count(0))
a.extend(b)
print(a)


