# 예외처리

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

print(9999)

try:
    f = open('Newfie2.txt', 'r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    print(data)
    f.close()

print("Its test")


try:
    f = open('Newfie.txt', 'r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    print(data)
    f.close()

print("Its test")

f = open('Newfie.txt', 'r')
try:
    data = f.read()
    print(data)
except Exception as e:
    print(e)
finally:
    f.close()


try:
    a = [1, 2]
    print(a[3])
    b = 4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")

print("테스트 입니다")


class Bird:
    def fly(b):
        raise NotImplemented
class Eagle(Bird):
    def fly(e):
       print("eagle in bird")
eagle = Eagle()
eagle.fly()












