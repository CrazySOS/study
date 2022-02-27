# 에러 및 예외처리
# Error

# 예외 종류
# 문법적으로는 에러가 없어도 코드실행 런타임 프로세스에서 발생하는 예외처리도 중요함
# linter : 코드스타일, 문법체크

# Syntax Error : 잘못된 문법
# print('a) // if True:  // x => y //
# 따옴표 하나가 없어서 신텍스 에러발생
# 함수나 반복문 등에서 ; 을 누락하여 신텍스 에러발생
# 파이썬에 없는 문법

# Name Error : 참조 변수가 없을때
# a = 10
# b = 15
# print(c) : C 가 없는데 C를 출력함

# ZeroDivisionError : 0으로 나누기 에러
# print(10/0)

# IndexError : 인덱스 범위 오버
#  x = [10, 20, 30]
# print(x[0]) : 10 출력됨
# print(x[3]) : index 3 에는 요소가 없음으로 에러 발생

# KeyError : 딕셔너리에서 키가 없음
# dic = {'name': 'kim', 'age': 18, 'Ciry': 'Seoul'}
# print(dic['hobby']) : hobby 라는 키가 없음으로 에러 발생
# 대안 : print(dic.get('hobby')) : 키가 없는 경우 None 출력함

# Attribute Error : 모듈, 클래스에 있는 잘못된 속성 사용시에 발생함 / 없는 메소드나 없는 값
# import time
# print(time.time())
# print(time.month()) : 없는 메소드라 에러 발생

# Value Error : 참조 값이 없을때
#  a = [1, 5, 9]
# a.remove(10) : 리스트에는 10이 없음으로 에러 발생

# Filenotfound Error : 파일을 찾을 수 없음
# q = open('test.txt', 'r') : 현재 경로에 해당 텍스트 파일이 없음으로 에러 발생

# Type Error : 타입이 없음/맞지 않음/ 호환불가
# x = [1, 2]
# y = (1, 2)
# z = 'test'
# print(x + y) : 리스트와 튜플은 합칠 수 없음 
# print(x + z) : str 과 리스트는 합칠 수 없다고 나옴
# 대안 : print(x + list(y)) : 형 변환해서 출력

# 코딩 순서
# 1. 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩하고
# 2. 그 후 런타임 예외 발생시 예외처리 코딩권장(EAPP 코딩스타일)

# Try : 에러명 1
# except : 에러명 2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 에러 발생하든 안하든 무조건 항상 실행




name = ['kim', 'lee', 'park']

try:
    z = 'kim' # 리스트에 없는 요소를 선택하면 에러 발생
    x = name.index(z) # x 는 z의 인덱스 값을 찾는 것
    print('{} found it! in name'. format(z, x+1)) 

except ValueError: # kim 이 없는 경우 벨류에러가 발생할 수 있음
# 어떤 에러가 발생하는지 모를때는 except: 또는 except Exception: 로 처리함
    print('Not found it! - Occurred Value Error') 
except IndexError:
    print('Not found it - Occurred Index Error')
# 발생할 수 있는 에러에 관해 최대한 except 를 선언해두고 (Value Error / IndexError)
except Exception: # 항상 except Exception 은 마지막에
    print('Not found it - Occurred Error')
# 그외 예측이 어려운 에러가 발생하는 경우 
else: # try 문이 정상적으로 실행됐을때 넘어옴
    print('Ok! else!')

finally: # try가 실행되든 expect가 실행되든 상관없이 무조건 실행
    print('Finally')


# 예외처리는 하지 않지만 무조건 수행되는 코딩패턴

try:
    print('Try')
finally:
    print('OK finally')
# 예외처리는 하지 않지만 실행되고 최후에 마지막으로 실행하고 빠져나가는 코딩패턴


# raise : raise 키워드로 예외 직접 발생

try:
    a = 'kim'
    if a == 'kim':
        print('Ok. 허가!')
    else:
        raise ValueError # Kim 이 아닌 사람은 밸류에러를 발생시킴
        # 벨류에러가 나오지 않고 원래 다른 에러가 나오지만 if를 만족 시키지 못하면 벨류에러로 처리한다는 것

except ValueError:
    print('문제 발생')
except Exception as f:
    print(f) # 에러내용을 f 로 선언하여 그대로 출력함
else:
    print('OK')










