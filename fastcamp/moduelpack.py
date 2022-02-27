# 패키지
# 상대경로
# --  .. : 부모디렉토리
# --  . : 현재 디렉토리

import builtins
from pack.fibonacci import Fibonacci

Fibonacci.fib(300)
print(Fibonacci.fib2(400))
print(Fibonacci().title)

from pack.fibonacci import * # 리소스를 많이 사용함으로 비권장

Fibonacci.fib(500)
print(Fibonacci.fib2(600))
print(Fibonacci().title)

from pack.fibonacci import Fibonacci as fb
# Fibonacci 라는 단어가 길어서 as 명령어를 통하여 Fibonacci를 fb로 줄여서 사용
fb.fib(1000)
print(fb.fib2(400))
print(fb().title)

import pack.cacuations as c

print(c.add(10, 100))
print(c.mul(10, 100))

from pack.cacuations import div as d

print(int(d(1000, 100)))

import pack.prints as p

p.print1()
p.print2()

print(dir(builtins)) # 빌트인 함수리스트, 별도로 임포트 할 필요없음, 기본셋팅

# __init__ : 파이썬2.x 버전에서 패키지 만들때 필수, 하위 호환을 위해서 생성해두는 것을 추천

# 단위실행 (독립적으로 파일 실행 / 단위테스트 할때 사용)
# if.__name__ == "__main__"
#    함수


















