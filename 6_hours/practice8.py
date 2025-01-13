# 클래스

# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
name = "마린"
hp = 40
damage = 5

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반모드 / 시즈모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format( \
        name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)

# 클래스 - 붕어빵 틀(기계)
# "서로 연관이 있는 함수와 변수의 집합" 정도로 이해

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
# -> 똑같은 하나의 클래스를 통해서 서로 다른 마린과 탱크 유닛을 만들 수 있음
 
# __init__ : 파이썬에서 쓰이는 생성자 

print("----------")
# 멤버변수

# 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # 추가 할당**

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태 입니다.".format(wraith2.name))

# if wraith1.clocking == True:
#     print("{0} 는 현재 클로킹 상태 입니다.".format(wraith2.name))
#     #-> 오류 발생 : AttributeError: 'Unit' object has no attribute 'clocking'

print("----------")
# 메소드
# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage)) 
            # location 은 self 없음, 전달 받은 값 사용한다는 의미

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다. ".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp)) 
        if self.hp <= 0 :
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃, 공격 유닛, 화염방사기
filebat1 = AttackUnit("파이어뱃", 50, 16)
filebat1.attack("5시")

# 공격 2 번 받는다고 가정
filebat1.damaged(25)
filebat1.damaged(25)

