# 함수 및 lamda

# 함수
# def 함수이름(parameter):
#   code

# 함수 호출
# 함수명(parameter)
# 함수선언 위치 중요

# 응용
def hello(world):
    print("Hello", world)

hello("python") # Hello python 출려
hello("777") # Hello 777 출력
# 함수를 사용할때는 함수를 먼저 선언 후 피라메터 입력

# 리턴이 있는 함수
def hello_return(world):
    val = "Hello " + str(world)
    return val

str = hello_return("love")
print(str)

# 다중 리턴
def fun_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = fun_mul(100)
print(val1, val2, val3)
print(type(val1), type(val2), type(val3))

# 다중 리턴 튜플출력
def fun_mul1(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

fun_mul12 = fun_mul(100)
print(fun_mul12, type(fun_mul12))

# *args / *kwargs
# 매개변수가 몇개가 넘어올지 모를때, 매개변수가 넘어오는 것에 따라서 함수의 작동을 달리할때 / 튜플타입
def args_fun(*args):
    print(args)

def args_func(*args): # * 가 1개일대는 튜플로 출력, 2개면 딕셔너리로 출력
    for a, b in enumerate(args): #enumerate : 인덱스와 벨류를 같이 불러옴
        print(a, b)
        
args_fun('kim')
args_fun('kim', 'park')
args_fun('kim', 'park', 'lee')

args_func('kim')
args_func('kim', 'park')
args_func('kim', 'park', 'lee')

def kwargs_fun(**kwargs):
    print(kwargs, type(kwargs))

def kwargs_func(**kwargs):
    for c, d in kwargs.items():
        print(c, d)

kwargs_fun(name1 = 'kim', name2 = 'park', name3 = 'lee')
kwargs_func(name1 = 'kim', name2 = 'park', name3 = 'lee')

# 혼합사용
def ex_m(arg1, arg2, *args, **kwargs): #arg1, arg2 는 필수로 받는 값, *arg 튜플형태로 받음, **kwargs 딕셔너리 형태로 받음 다양한 데이터를 가변적으로 받아서 함수를 보다 고도화 되어 기능을 함축해서 사용가능
    print(arg1, arg2, args, kwargs)
    
ex_m(10, 20)
ex_m(10, 20, 'park', 'lee', age=24, age2=35)

# 중첩함수 (python decorator)

def nes_fun(num):
    def nes_in_fun(num):
        print(num)
    print(nes_in_fun)
    return nes_in_fun(num + 10000)
    
nes_fun(10000)

# hint

def fun_mul2(x : int) -> list: # x는 정수여야 하고 이 함수는 리스트로 반환한다는 뜻
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

print(fun_mul2(5))

#ㅣamda 식 -> 메모리 절약, 가독성향상, 코드 간결
# 함수는 객체를 생성 후 리소스 할당되는데 람다는 즉시실행하여 heap초기화 되며  메모리가 초기화된다.

# 일반적함수 > 변수할당

def mul_10(nim : int) -> int:
    return nim * 10

var_fun = mul_10
print(var_fun) # <function mul_10 at 0x1003761f0> 출력됨
print(type(var_fun)) # <class 'function'> 으로 출력됨
print(var_fun(10)) # 100 출력

# 위 함수를 람다식으로 변경
lambda_mul_10 = lambda num : num * 10 # num 은 nim과 같다
print(lambda_mul_10(10)) 

# 람다를 사용함으로써 코드를 간결하게 쓸 수 있다. 
# 데이터 전처리나 데이터베이스에서 사용하는 게시판 데이터 같은 것을 대량으로 가져와서 날짜 변경이나 내용수정, 문자열을 연결해서 새로운 문자열 제작 등등 에 활용

def fun(x, y, func):
    print(x * y * func(10))
    
fun(10, 10, lambda_mul_10)
fun(10, 10, lambda x : x * 1000)










