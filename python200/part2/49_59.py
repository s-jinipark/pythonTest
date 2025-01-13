'''
049 클래스 이해하기(class)
050 클래스 멤버와 인스턴스 멤버 이해하기
051 클래스 메소드 이해하기
052 클래스 생성자 이해하기
053 클래스 소멸자 이해하기
054 클래스 상속 이해하기
055 예외처리 이해하기 ① (try~except)
056 예외처리 이해하기 ② (try~except~else)
057 예외처리 이해하기 ③ (try~except~finally)
058 예외처리 이해하기 ④ (try~except Exception as e)
059 예외처리 이해하기 ⑤ (try~except 특정 예외)
'''

##################################################
print("049 클래스 이해하기(class)")
class MyClas :
    var = '안녕하세요'
    def sayHello(self):
        print(self.var)

obj = MyClas()
print(obj.var)
print(obj.sayHello())
# 안녕하세요
# None     (-> ?? 출력됨)

'''
클래스는 프로그래머가 지정한 이름으로 만든 하나의 독립된 공간이며,
이름공간(name space) 이라 불림

class 클래스 이름 :
  클래스 멤버 정의
  클래스 메소드 정의

클래스 메소드는 클래스 내에서 정의되는 함수
클래스 메소드는 첫번째 인자가 반드시 self 로 시작해야 함
self 는 이 클래스의 인스턴스 객체를 가리키는 참조자임
'''


##################################################
print("050 클래스 멤버와 인스턴스 멤버 이해하기")
class MyClass50:
    var = '안녕하세요(50)'
    def sayHello(self):
        param1 = '안녕'
        self.param2 = '하이'
        print(param1)
        print(self.var)

obj = MyClass50()
print(obj.var)
obj.sayHello()
#print(MyClass50.var)
#print(obj.param1) # -> AttributeError: 'MyClass50' object has no attribute 'param1'
# => param1 은 sayHello() 의 지역변수이므로 MyClass50 의 인스턴스 객체인 obj 의 멤버로 참조가 불가능

'''
클래스 멤버 var 는 다음과 같이 참조할 수 있음
self.var        # 클래스 매소드 내에서 var 를 참조할 경우
MyClass50.var   # 클래스 밖에서 클래스 이름만으로 참조할 경우(별로 안 쓰임)
obj.var         # MyClass50 의 인스턴스 객체 obj 에서 var 를 참조할 경우 
'''


##################################################
print("051 클래스 메소드 이해하기")
class MyClass51:
    def sayHello(self):
        print('안녕하세요')
    def sayBye(self, name):
        print('%s ! 다음에 보자 !'%name)

obj = MyClass51()
obj.sayHello()
obj.sayBye('철수')


##################################################
print("052 클래스 생성자 이해하기")
class MyClass52:
    def __init__(self):
        self.var = '안녕하세요!'
        print('MyClass52 인스턴스 객체가 생성되었습니다.')

obj = MyClass52()
print(obj.var)

'''
 클래스 생성자는 인자를 가질 수 있음
 생성자에 인자가 있다면 인스턴스 객체를 만들 때
  인자에 적당한 값을 대입해 주어야 함
'''

##################################################
print("053 클래스 소멸자 이해하기")
class MyClass53:
    def __del__(self):
        print('MyClass53 인스턴스 객체가 메모리에서 제거됩니다.')

obj = MyClass53()
del obj


##################################################
print("054 클래스 상속 이해하기")
class Add:
    def add(self, n1, n2):
        return n1+n2

class Calculator(Add) :
    def sub(self, n1, n2):
        return n1-n2

obj = Calculator()
print(obj.add(1, 2))
print(obj.sub(1, 2))

'''
class 자식클래스(부모클래스):

만약 자식 클래스에서 부모클래스로부터 상속받은 멤버나 메소드와 
동일한 이름의 멤버나 메소드가 존재하면 자식클래스의 것이 우선함

자식 클래스는 여러 개의 부모 클래스로부터 상속 받을 수 있음
이를 다중상속 이라 함

class 자식클래스(부모클래스1, 부모클래스2): 

'''


##################################################
print("055 예외처리 이해하기 ① (try~except)")

try :
    print('안녕하세요')
    print(param)
except :
    print('예외 발생 !')


##################################################
print("056 예외처리 이해하기 ② (try~except~else)")
try :
    print('안녕')
    #print(param)
except :
    print('에외 발생')
else:
    print('예외 발생 안함')


##################################################
print("057 예외처리 이해하기 ③ (try~except~finally)")
try :
    print('안녕')
    print(param)
except :
    print('에외 발생')
finally:
    print('무조건 실행하는 코드')


##################################################
print("058 예외처리 이해하기 ④ (try~except Exception as e)")
try :
    print('안녕')
    print(param)
except Exception as e:
    print(e)

# name 'param' is not defined [이 출력됨]


##################################################
print("059 예외처리 이해하기 ⑤ (try~except 특정 예외)")
import time
count = 1
try:
    while True:
        print(count)
        count += 1
        time.sleep(0.5)
except KeyboardInterrupt :
    print('사용자에 의해 프로그램이 중단되었음')

