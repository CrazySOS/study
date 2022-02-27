class Fibonacci:
    def __init__(self, title="Fibonacci"):
        self.title = title
        
    def fib(n):
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a+b
        print()
        
    def fib2(n): # 리스트형태로 반환하는 fib클래스
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a+b
        return result


# Fibonacci 클래스 안에는 Fibonacci를 출력해주는 함수 fib 와 리스트로 만들어서 result로 반환하는 함수 fib2가 있다
# 패키지형태가 pack 폴더안에 fibonacci.py 파일안에 Fibonacci 클래스 안에 함수가 있는 형태



