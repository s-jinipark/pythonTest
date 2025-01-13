# 281 클래스 정의
# 다음 코드가 동작하도록 차 클래스를 정의하세요.

# >> car = 차(2, 1000)
# >> car.바퀴
# 2
# >> car.가격
# 1000
class Car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

car = Car(2, 1000)
print(car.wheel)
#  정답확인

# 282 클래스 상속
# 차 클래스를 상속받은 자전차 클래스를 정의하세요.

class Bicycle(Car):
    pass
#  정답확인

# 283 클래스 상속
# 다음 코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.

# >> bicycle = 자전차(2, 100)
# >> bicycle.가격
# 100

bicycle = Bicycle(3, 200)
print(bicycle.price)
#  정답확인

# 284 클래스 상속
# 다음 코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.

# >> bicycle = 자전차(2, 100, "시마노")
# >> bicycle.구동계
# 시마노

#  정답확인
class AutoCar(Car):
    def __init__(self, wheel, price, gear):
        #super.__init__(wheel, price)  #-> 오류
        super().__init__(wheel, price) 
        self.gear = gear

print("-----")
bicycle2 = AutoCar(2, 100, "시마노")
print(bicycle2.gear)
print(bicycle2.wheel)

# 285 클래스 상속
# 다음 코드가 동작하도록 차 클래스를 상속받는 자동차 클래스를 정의하세요.

# >> car = 자동차(4, 1000)
# >> car.정보()
# 바퀴수 4
# 가격 1000
#  정답확인
class AutoCar285(Car):
    def __init__(self, wheel, price):
        super().__init__(wheel, price)

    def info(self):
        print("바퀴 수", self.wheel)
        print("가격", self.price)

print("-----")
autocar285 = AutoCar285(4, 1000)
autocar285.info()

# 286 부모 클래스 생성자 호출
# 다음 코드가 동작하도록 자전차 클래스를 수정하세요.

# >> bicycle = 자전차(2, 100, "시마노")
# >> bicycle.정보()
# 바퀴수 2
# 가격 100
#  정답확인
class Car286:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price
    def info(self):
        print("바퀴수", self.wheel)
        print("가격", self.price)

class AutoCar286(Car286):
    def __init__(self, wheel, price, gear):
        super().__init__(wheel, price)
        self.gear = gear 

print("-----")
bicycle286 = AutoCar286(3, 120, "시마노")
bicycle286.info()

# 287 부모 클래스 메서드 호출
# 자전차의 정보() 메서드로 구동계 정보까지 출력하도록 수정해보세요.

# >> bicycle = 자전차(2, 100, "시마노")
# >> bicycle.정보()
# 바퀴수 2
# 가격 100
# 구동계 시마노
#  정답확인
class AutoCar286_2(Car286):
    def __init__(self, wheel, price, gear):
        super().__init__(wheel, price)
        self.gear = gear 

    def info(self):
        super().info()  # <- 부모 클래스 메서드 호출
        print("구동계", self.gear)

print("-----")
bicycle286_2 = AutoCar286_2(5, 150, "시마노2")
bicycle286_2.info()

# 288 메서드 오버라이딩
# 다음 코드의 실행 결과를 예상해보세요.

# class 부모:
#   def 호출(self):
#     print("부모호출")

# class 자식(부모):
#   def 호출(self):
#     print("자식호출")
# 나 = 자식()
# 나.호출()
#  정답확인
#=> 자식호출

# 289 생성자
# 다음 코드의 실행 결과를 예상해보세요.

# class 부모:
#   def __init__(self):
#     print("부모생성")

# class 자식(부모):
#   def __init__(self):
#     print("자식생성")
# 나 = 자식()
#  정답확인
#=> 자식생성 (** 부모생성은 호출 안했기 때문...)

# 290 부모클래스 생성자 호출
# 다음 코드의 실행 결과를 예상해보세요.

class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()
#  정답확인
#=> 자식생성
#=> 부모생성
