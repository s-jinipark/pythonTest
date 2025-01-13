# 271 Account 클래스
# 은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다. 
# Account 클래스를 생성한 후 생성자를 구현해보세요. 생성자에서는 예금주와 초기 잔액만 입력 받습니다. 
# 은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.

# 은행이름: SC은행
# 계좌번호: 111-11-111111
#  정답확인
import random

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.account_no = num1 + "-" + num2 + "-" + num3

kim = Account("김민수", 200000)
print(kim.balance)
print(kim.account_no)

# 272 클래스 변수
# 클래스 변수를 사용해서 Account 클래스로부터 생성된 계좌 객체의 개수를 저장하세요.

#  정답확인
class Account272:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.account_no = num1 + "-" + num2 + "-" + num3
        Account272.account_count += 1

kim = Account272("김민수", 100)
print(Account272.account_count)
lee = Account272("이민수", 200)
print(Account272.account_count)

# 273 클래스 변수 출력
# Account 클래스로부터 생성된 계좌의 개수를 출력하는 get_account_num() 메서드를 추가하세요.

#  정답확인
class Account273:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.account_no = num1 + "-" + num2 + "-" + num3
        Account273.account_count += 1
    
    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

print("-----")
kim = Account273("김민수", 100)
lee = Account273("이민수", 200)
kim.get_account_num()
lee.get_account_num()

# 274 입금 메서드
# Account 클래스에 입금을 위한 deposit 메서드를 추가하세요. 입금은 최소 1원 이상만 가능합니다.

#  정답확인
class Account274:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.account_no = num1 + "-" + num2 + "-" + num3
        Account274.account_count += 1
    
    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

print("-----")
kim = Account274("김민수", 100)
kim.deposit(100)
print(kim.balance)

# 275 출금 메서드
# Account 클래스에 출금을 위한 withdraw 메서드를 추가하세요. 
# 출금은 계좌의 잔고 이상으로 출금할 수는 없습니다.

#  정답확인
class Account275:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.account_no = num1 + "-" + num2 + "-" + num3
        Account275.account_count += 1
    
    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

print("-----")
kim = Account275("김민수", 100)
kim.deposit(100)
print(kim.balance)
kim.withdraw(100)
print(kim.balance)
kim.withdraw(100)
print(kim.balance)

# 276 정보 출력 메서드
# Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를 추가하세요. 
# 잔고는 세자리마다 쉼표를 출력하세요.

# 은행이름: SC은행
# 예금주: 파이썬
# 계좌번호: 111-11-111111
# 잔고: 10,000원
#  정답확인
class Account276:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.account_no = num1 + "-" + num2 + "-" + num3
        Account276.account_count += 1
    
    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def display_info(self):
        print("은행이름 : " + self.bank)
        print("예금주   : " + self.name)
        print("계좌번호 : " + self.account_no)
        print("잔고     : " + str(self.balance))       

print("-----")
kim = Account276("김민수", 100000)
kim.display_info()

# 277 이자 지급하기
# 입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 코드를 변경해보세요.

#  정답확인
class Account277:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0  # 입금 횟수

        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.account_no = num1 + "-" + num2 + "-" + num3
        Account277.account_count += 1
    
    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
            self.deposit_count += 1
            if self.deposit_count%5 == 0 :
                self.balance = self.balance * 1.01

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def display_info(self):
        print("은행이름 : " + self.bank)
        print("예금주   : " + self.name)
        print("계좌번호 : " + self.account_no)
        print("잔고     : " + str(self.balance))       

print("-----")
kim = Account277("김민수", 10000)
kim.deposit(5000)
kim.deposit(5000)
kim.deposit(5000)
kim.deposit(5000)
kim.deposit(5000)
print(kim.balance)
print(kim.deposit_count)

# 278 여러 객체 생성
# Account 클래스로부터 3개 이상 인스턴스를 생성하고 생성된 인스턴스를 리스트에 저장해보세요.

print("-----")
lst = []
a1 = Account277("이승윤", 100)
lst.append(a1)
a2 = Account277("정홍일", 100)
lst.append(a2)
a3 = Account277("이무진", 100)
lst.append(a3)
print(lst)
#  정답확인

# 279 객체 순회
# 반복문을 통해 리스트에 있는 객체를 순회하면서 잔고가 100만원 이상인 고객의 정보만 출력하세요.

#  정답확인
print("-----")
data = []
d1 = Account277("이승윤", 10000)
data.append(d1)
d2 = Account277("정홍일", 5000)
data.append(d2)
d3 = Account277("이무진", 11000)
data.append(d3)

for d in data:
    if d.balance >= 10000 :  # 만원이상
        #print(d.name + " : " + str(d.balance))
        d.display_info()

# 280 입출금 내역
# 입금과 출금 내역이 기록되도록 코드를 업데이트 하세요. 
# 입금 내역과 출금 내역을 출력하는 deposit_history와 withdraw_history 메서드를 추가하세요.

#  정답확인
class Account280:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0  # 입금 횟수
        self.deposit_log = []   # 입금 내역
        self.withdraw_log = []  # 출금 내역

        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.account_no = num1 + "-" + num2 + "-" + num3
        Account280.account_count += 1
    
    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
            self.deposit_count += 1
            self.deposit_log.append(amount)
            if self.deposit_count%5 == 0 :
                self.balance = self.balance * 1.01

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.withdraw_log.append(amount)

    def display_info(self):
        print("은행이름 : " + self.bank)
        print("예금주   : " + self.name)
        print("계좌번호 : " + self.account_no)
        print("잔고     : " + str(self.balance))       

    def deposit_history(self):
        for d in self.deposit_log:
            print(d)

    def withdraw_history(self):
        for w in self.withdraw_log:
            print(w)

print("-----")
kim = Account280("김민수", 10000)
kim.deposit(5000)
kim.deposit(5000)
kim.deposit(5000)
kim.withdraw(5000)
kim.withdraw(5000)
print("deposit_history")
kim.deposit_history()
print("-----")
print("withdraw_history")
kim.withdraw_history()