# Lambda함수

mylist = [lambda a, b: a+b, lambda a, b: a*b]

print(mylist[0](1, 2))
print(mylist[1](1, 2))

# 사용자 입력 과 출력

s = input("숫자를 입력하세요:")
print(s)

print("life""is""so good")
print("life"+"is"+"so good")
print("life","is","so good")

f = open("Newfie.txt", 'w')
f.close

# 파일 쓰기
f = open("/Users/youngsoonsong/Desktop/study/Newfie.txt", 'w', encoding='utf8')
for i in range(1, 11):
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 파일 읽기
f = open("/Users/youngsoonsong/Desktop/study/Newfie.txt", 'r')
line = f.readline()
print(line)
f.close()

f = open("/Users/youngsoonsong/Desktop/study/Newfie.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f = open("/Users/youngsoonsong/Desktop/study/Newfie.txt", 'r', encoding='utf8')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open("/Users/youngsoonsong/Desktop/study/Newfie.txt", 'r', encoding='utf8')
lines = f.readlines()
for line in lines:
    print(line.strip("\n"))
f.close()

f = open("/Users/youngsoonsong/Desktop/study/Newfie.txt", 'r', encoding='utf8')
lines = f.readlines()
for line in lines:
    print(line.strip("\n"), end=" ")
f.close()

f = open("/Users/youngsoonsong/Desktop/study/Newfie.txt", 'r', encoding='utf8')
data = f.read()
print(data)
f.close()

f = open("/Users/youngsoonsong/Desktop/study/Newfie.txt", 'a', encoding='utf8')
for i in range(11, 20):
    data = "%d번째 줄 입니다.\n" % i
    f.write(data)
f.close()

with open("/Users/youngsoonsong/Desktop/study/newfie.txt", "w") as f:
    f.write("life is too short, u need python")





