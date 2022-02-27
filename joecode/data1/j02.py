# 딕셔너리

# dic={'name':'josefien', 'age':'37', 'birth':'0611', 'phone':'83416165'}
# print(dic['name'])

a = {1: "joy"}
a[2] = "enjoy"
print(a)

del a[1]
print(a)

a[1] = "love"
a[3] = "smail"
a[4] = "story"
print(a)
print(a[3])

b = {"name": "josefien", "phone":"83416165", "birth":"0611"}

print(b.keys())
print(b.values())
print(b.items())

for K in b.keys():
    print(K)

for V in b.values():
    print(V)

for k, v in b.items():
    print('키는: ' + str(k))
    print('벨류는: ' + v)

print(b.get("name"))
print(b.get("add"))
print(b.get("add", "없음"))

print("add" in b)
print("name" in b)








