# 변수

a = [1, 2, 3]
# b = a
b = a[:]
a[1] = 4
print(b)

print(id(a))
print(id(b))

print(a is b)

print(b)
print(a)

print(id(a))
print(id(b))

from copy import copy
q = [1, 2, 3]
w = copy(q)
q[1] = 4

print(q)
print(w)
print(id(q))
print(id(w))

c, d = ["python", "life"] #튜플은 괄호가 ()로 이용
print(c)
print(d)

e = f = "hello"
print(e)
print(f)

g = 3
h = 4

tmp = h
h = g
g = tmp

print(g)
print(h)


g, h = h, g

print(g)
print(h)



