#입력과 출력

def sum(a, b):
    result = a + b
    return result
print(sum(1, 2))

def say():
    return 'hi'
print(say())

def sum(c, d):
    print("%d, %d 의 합은 %d 입니다." %(c, d, c+d))
sum(1, 2)

def suny(*args):
    sun = 0
    for i in args:
        sun = sun + i
    return sun
print(suny(1, 2, 3))

def sunyy(*args):
    suni = 0
    for i in args:
        suni = suni + i
    return suni
print(sunyy(1, 2, 3, 4, 5))

def print_kwargs(**kwargs):
    for k in kwargs.keys():
        if(k == "name"):
            print("당신의 이름은 :" + kwargs.get(k))
print_kwargs(name="josefien", age="37", char="great")

def sum_and_mul(a, b):
    return a+b, a*b
print(sum_and_mul(1, 2))

a = 1

def var(a):
    a = a + 1
var(a)
print(a)

def var(a):
    a = a + 1
    return a # 함수밖으로 a값을 빼줌
a = var(a)
print(a)

b = 1
def vartest():
    global b # 함수밖에 글로벌라인에 있는 a의 값을 가져온다
    b = b + 1
vartest()
print(b)









