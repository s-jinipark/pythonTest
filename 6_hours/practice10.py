# 오버라이딩

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp 
        self.speed = speed #-> [2] speed 추가
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit):  # 일반 유닛을 상속 받아서 만듬
    def __init__(self, name, hp, speed, damage): #-> [2] speed 추가
        Unit.__init__(self, name, hp,speed) #-> [2] speed 추가
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

print("----------")
# 다중 상속

# 드랍쉽 : 공중유닛, 수송기, 마린/파이어뱃/탱크 등을 수송. 공격 X

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))    

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) #-> [2] speed 0 으로
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# # 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# 벌처 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌처", 80, 10, 20)

# 배틀크루져 : 곧중 유닛, 체력도 굉장히 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")

battlecruiser.fly(battlecruiser.name, "9시")
# -> 날 수 있는 유닛인지 확인 후 fly 를 쓰기 귀찮음
# FlyableAttackUnit 에 move 라는 메소드를 만들어 줌(오버라이딩) =>> 재정의
battlecruiser.move("9시")


print("----------")
# pass

# class BuildingUint(Unit):
#     def __init__(self, name, hp, location):
#         pass

# # 서플라이 디폿 : 건물, 1개 건물 = 8 유닛
# supply_depot = BuildingUint("서플라이 디폿", 500, "7시")

# # 그냥 넘어감

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()


print("----------")
# super

class BuildingUint(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # -> 다중 상속일 경우는 안됨
        self.location = location