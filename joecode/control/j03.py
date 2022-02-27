#for 

from ast import Continue


test_list = ['one','two','three']
for i in test_list:
    print(i)

q = [(1, 2), (3, 4), (5,6)]
for (first, last) in q:
    print(first + last)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)
        
    if mark >= 60: 
        print("%d번 학생은 합격입니다. 축하합니다." % number)

sum = 0
for w in range(1, 11):
    sum = sum + w
print(sum)

for a in range(2, 10):
    for s in range(1, 10):
        print(a * s, end=" ")
    print(' ')



f = [1, 2, 3, 4, 5]
d = [num * 3 for num in f]
print(d)

g = [num * 3 for num in f if num % 2 == 0]
print(g)

z = [x * y for x in range(2, 10) for y in range(1, 10)]
print(z)
