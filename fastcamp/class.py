# 클래스와 상속

# 클래스 선언
# class classname:
#    함수

# 응용

class UserInfo:
    # 클래스의 구성 : 속성, 메소드
    def __init__(self, name):
        self.name = name
    def userinfo_p(self):
        print(self.name)

# 네임스페이스 : user1 과 user2 가 각각 독립적인 개체임으로 주소가 다르다.
user1 = UserInfo("lee")
user1.userinfo_p()
user2 = UserInfo("park")
user2.userinfo_p()

print(id(user1.name))
print(id(user2.name))
print(user1.__dict__)
print(user2.__dict__)

# self의 이해

class SelfTest():
    def fun1(): # self 가 없음으로 클래스 이름으로 호출
        print('fun1 called!')
    def fun2(self): # self 가 있음으로 인스턴스를 입력
        print(id(self))
        print('fun2 called!!')
        
SelfTest.fun1()

selft = SelfTest()
selft.fun2()

print(id(selft))


# 클래스변수, 인스턴스변수

class WareHouse:
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('kim')
user2 = WareHouse('park')
user3 = WareHouse('lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

print(WareHouse.__dict__) # 네임스페이스 각각 지정, 클래스 변수 공유 // 출력된 부분중 'stock_num': 3 확인

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num) # 자기 네임스페이스에 없으면 클래스 네임스페이스가서 변수를 찾고 거기에도 없으면 에러발생(뭔소리여)
print(user2.stock_num)
print(user3.stock_num)

del user1

# print(user1.stock_num) => user1 을  삭제하여 해당 코드는 오류가 발생함 
print(user2.stock_num)
print(user3.stock_num)

# 상속 / 다중상속
# 부모클래스(슈퍼클래스) 및 자식클래스(서브클래스) => 모든 속성, 메소드 사용가능
# 예시
# 라면 - 속성(종류, 회사, 이름 등등 공통으로 쓸 수 있는 속성) : 부모클래스
# 라면 - 부모클래스를 불러오고 거기에 맛, 면종류 등의 속성 추가 : 자식클래스

class Car:
    'parent class'
    def __init__(self, tp, brand):
        self.tp = tp
        self.brand = brand
    
    def show(show):
        return 'Car Clasdd "Show Method"'

class NewCar(Car):
    'sub class'
    def __init__(self, car_model, tp, brand):
        super().__init__(tp, brand) # 부모 클래스의 __init__을 불러옴
        self.car_model = car_model
    
    def show_model(sm) -> None:
        return "Your Car Name : %s" % sm.car_model
    

class OldCar(Car):
    'sub class'
    def __init__(self, car_model, tp, brand):
        super().__init__(tp, brand) # 부모 클래스의 __init__을 불러옴
        self.car_model = car_model
    
    def show_model(sm) -> None:
        return "Your Car Name : %s" % sm.car_model

    def show(self):
        print(super().show()) # 부모의 메소드를 같이 출력
        return 'Car info : %s, %s, %s' %(self.car_model, self.tp, self.brand)
# 위함수를 사용하는 방법

Model1 = NewCar('520d', 'sedan', 'BMW ')
print(Model1.brand) # super
print(Model1.tp) # super
print(Model1.car_model) #sub
print(Model1.show()) # super
print(Model1.show_model()) # sub
print(Model1.__dict__)


# 오버라이딩
Model2 = OldCar("220d", 'suv', 'Benz')
print(Model2.show()) # super 의 show가 반영되지 않고 sub에서 내용을 변경한 show가 반영됨 / 덮어쓰기가 됨(업로드 등)

# Parent 클래스의 메소드 콜
Model3 = OldCar("350s", 'sedan', 'Benz')
print(Model3.show())

# Inheritance Info : 상속이 길때 각 요소의 info를 보여줌
print(NewCar.mro())
# [<class '__main__.NewCar'>, <class '__main__.Car'>, <class 'object'>] 출력됨
# NewCar 클래스는 Car클래스의 상속을 받았고 Car클래스는 오브젝트 클래스의 상속을 받는다
# 오브젝트 클래스란 파이썬의 모든 클래스의 부모다.
# mro()는 소스를 파악할때 자주 사용하는 것으로 상속정보를 리스트형태로 반환해줌
print(OldCar.mro())


# 다중 상속

class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

print(M.mro())





























