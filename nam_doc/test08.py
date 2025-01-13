
# 클래스 

# class FishCakeMaker:
#     def __init__(self, param):  # 클래스가 최초 생성될 때 호출됨
#         self._fish_name = param    # 클래스의 멤버 함수와 변수에는 항상 self
#         pass
#     def show_name(self):
#         print(self._fish_name)

# fish = FishCakeMaker("붕어빵")
# fish.show_name()


class FishCakeMaker:
    def __init__(self, **kwargs):
        self._size = 10     #-> 기본값
        self._flavor = "팥"
        self._price = 100
        if "size" in kwargs:
            self._size = kwargs.get("size")
        if "flavor" in kwargs:
            self._flavor = kwargs.get("flavor")  
        if "price" in kwargs:
            self._price = kwargs.get("price")  

    # [2]
    def __str__(self):
        return "<class FishCakeMaker (size={}, price={}, flaver={})>".format(self._size, self._price, self._flavor)

    def show(self):
        print("붕어빵 종류 {}".format(self._flavor))
        print("붕어빵 크기 {}".format(self._size))
        print("붕어빵 가격 {}".format(self._price))
        print("*" * 60)
fish1 = FishCakeMaker()
fish2 = FishCakeMaker(size=20, price=300)
fish3 = FishCakeMaker(size=15, price=500, flavor="초콜렛")

fish1.show()
fish2.show()
fish3.show()

print(fish1)

# [3]
# 상속
class MarketGoods(FishCakeMaker):
    def __init__(self, margin=1000, **kwargs):
        super().__init__(**kwargs)
        self._market_price = self._price + margin
    def show(self):
        print(self._flavor, self._market_price)

fish11 = MarketGoods(size=20, price=500)
fish11.show()
