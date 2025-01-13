

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

# [3]
# 상속
class MarketGoods(FishCakeMaker):
    def __init__(self, margin=1000, **kwargs):
        super().__init__(**kwargs)
        self._market_price = self._price + margin
    def show(self):
        print(self._flavor, self._market_price)

if __name__ == "__main__" :
    fish11 = MarketGoods(size=20, price=500)
    fish11.show()
