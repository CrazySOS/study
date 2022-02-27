#집합

s1 = set([1, 2, 3, 4, 5])
s2 = {1,2,3}
print(s1)
print(s2)
print(type(s1), type(s2))

s3 = set('hello')
print(s3)

q = [1, 2, 2, 3, 4, 4, 5]
w = list(set(q))
print(w)


z1 = set([1, 2, 3, 4, 5, 6])
z2 = set([4, 5, 6, 7, 8, 9])

print(z1 & z2)
print(z1.intersection(z2))

print(z1 | z2)
print(z1.union(z2))

print(z1 - z2)
print(z1.difference(z2))

z1.add(0)
print(z1)

z2.update([10, 11, 12])
print(z2)

z2.remove(12)
print(z2)



# 불
a = True
if a :
    print(a)
b = '안녕'
if b :
    print(b)
c = ""
if c:
    print(c)

f = [1, 2, 3, 4]

if f:
    print(f)
    
while f:
    f.pop()
    print(f)
















