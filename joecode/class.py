#  클래스

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))


class Person:
  def __init__(my, name, age):
    my.name = name
    my.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Calculator:
    def __init__(abc):
        abc.result = 0

    def add(asd, num):
        asd.result += num
        return asd.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

class Person:
  def __init__(mine, name, age):
    mine.name = name
    mine.age = age

  def myfunc(insa):
    print("Hello my name is " + insa.name + " Hello, I'm " + str(insa.age) + " years old")

p1 = Person("John", 36)
p1.age = 40 # 나이를 수정함
p1.name = "Sujan"
# print(p1.age) # 40으로 출력됨
p1.myfunc()


class Four:
    def __init__(any, first, second):
        any.first = first
        any.second = second
    def setdata(num, first, second):
        num.first = first
        num.second = second
    def add(plus):
        result = plus.first + plus.second
        return result
    def mul(mul):
        result = mul.first * mul.second
        return result
    def sub(sub):
        result = sub.first - sub.second
        return result
    def div(div):
        result = div.first / div.second
        return result

a = Four(4, 2)
# a.setdata(4, 2) #__init__  이 없을때 a = Four() 하고 다음 숫자 입력란에 뭐가 올지 기재

print(a.first)
print(a.second)

print(a.add())


# 클래스 상속

class MFour(Four): # Four 클래스를 가져온다는 뜻
    pass

b = MFour(4, 2)
print(b.add())


class MoFour(Four):
    def pow(pow):
        result = pow.first ** pow.second
        return result

c = MoFour(4, 2)
print(c.pow())


class SFour(Four):
    def div(div):
        if div.second == 0:
            return 0
        else:
            return div.first / div.second

d = SFour(4, 0)
print(d.div())










