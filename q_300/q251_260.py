# 251 클래스, 객체, 인스턴스
# 클래스, 객체, 인스턴스에 대해 설명해봅시다.

#  정답확인

# 252 클래스 정의
# 비어있는 사람 (Human) 클래스를 "정의" 해보세요.

#  정답확인
# class Human:
#     pass

# 253 인스턴스 생성
# 사람 (Human) 클래스의 인스턴스를 "생성" 하고 이를 areum 변수로 바인딩해보세요.

#  정답확인
# areum = Human()

# 254 클래스 생성자-1
# 사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가하세요.

# >>> areum = Human()
# 응애응애
class Human254:
    def __init__(self):
        print("응애")

areum = Human254()
#  정답확인

# 255 클래스 생성자-2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.

# >>> areum = Human("아름", 25, "여자")
#  정답확인
class Human255:
    def __init__(self, name, age, sex) :
        self.name = name
        self.age = age
        self.sex = sex

areum = Human255("아름", 25, "여자")    
print(areum.name)

# 256 인스턴스 속성에 접근
# 255에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요. 인스턴스 변수에 접근하여 값을 출력하면 됩니다.

# 이름: 조아름, 나이: 25, 성별: 여자
# 인스턴스 변수에 접근하여 값을 가져오는 예

# >>> areum.age
# 25
#  정답확인
print(areum.age)

# 257 클래스 메소드 - 1
# 사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.

# >>> areum.who()
# 이름: 조아름, 나이: 25, 성별: 여자
class Human257:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def who(self):
        print("이름: "+ self.name +", 나이: "+ str(self.age) +", 성별: "+self.sex)

h257 = Human257("조아름", 25, "여자") 
h257.who()

#  정답확인

# 258 클래스 메소드 - 2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.

# >>> areum = Human("모름", 0, "모름")
# >>> areum.setInfo("아름", 25, "여자")
class Human258:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def who(self):
        print("이름: "+ self.name +", 나이: "+ str(self.age) +", 성별: "+self.sex)

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

print("----- -----")       
h258 = Human258("조아름", 25, "여자") 
h258.who()
h258.setInfo("아름", 26, "여자")
h258.who()
#  정답확인

# 259 클래스 소멸자
# 사람 (human) 클래스에 "나의 죽음을 알리지 말라"를 출력하는 소멸자를 추가하세요.

# >>> areum = Human("아름", 25, "여자")
# >>> del areum
# 나의 죽음을 알리지 말라
class Human259:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def who(self):
        print("이름: "+ self.name +", 나이: "+ str(self.age) +", 성별: "+self.sex)

    def __del__(self):
        print("나의 죽음을 알리지 말라")

print("----- -----")     
h259 = Human259("조아름", 25, "여자") 
del(h259)

#  정답확인
# 260 에러의 원인
# 아래와 같은 에러가 발생한 원인에 대해 설명하세요.

# class OMG : 
#     def print() :
#         print("Oh my god")

# >>> >>> myStock = OMG()
# >>> myStock.print()
# TypeError Traceback (most recent call last)
# <ipython-input-233-c85c04535b22> in <module>()
# ----> myStock.print()

# TypeError: print() takes 0 positional arguments but 1 was given
#  정답확인

class OMG :
    def print() :  #def print(self) :
        print("Oh my god")


mystock = OMG()
mystock.print()      # OMG.print(mystock)
