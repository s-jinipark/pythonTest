# 261 Stock 클래스 생성
# 주식 종목에 대한 정보를 저장하는 Stock 클래스를 정의해보세요. 
# 클래스는 속성과 메서드를 갖고 있지 않습니다.

#  정답확인
class Stock261:
    pass

# 262 생성자
# Stock 클래스의 객체가 생성될 때 종목명과 종목코드를 입력 받을 수 있도록 생성자를 정의해보세요.

# 삼성 = Stock("삼성전자", "005930")
class Stock262:
    def __init__(self, st_name, st_code):
        self.st_name = st_name
        self.st_code = st_code

ss = Stock262("삼성전자", "005930")
print(ss.st_name)
print(ss.st_code)

#  정답확인

# 263 메서드
# 객체에 종목명을 입력할 수 있는 set_name 메서드를 추가해보세요.
class Stock263:
    def __init__(self, st_name, st_code):
        self.st_name = st_name
        self.st_code = st_code
    def set_name(self, st_name):
        self.st_name = st_name
print("----- -----")
s263 = Stock263(None, None)
s263.set_name("삼성전자")
print(s263.st_name)
# a = Stock(None, None)
# a.set_name("삼성전자")

#  정답확인

# 264 메서드
# 객체에 종목코드를 입력할 수 있는 set_code 메서드를 추가해보세요.

# a = Stock(None, None)
# a.set_code("005930")
class Stock264:
    def __init__(self, st_name, st_code):
        self.st_name = st_name
        self.st_code = st_code
    def set_code(self, st_code):
        self.st_code = st_code

s264 = Stock264(None, None)
s264.set_code("005930")
print(s264.st_code)

#  정답확인

# 265 메서드
# 종목명과 종목코드를 리턴하는 get_name, get_code 메서드를 추가하세요. 
# 해당 메서드를 사용하여 종목명과 종목코드를 얻고 이를 출력해보세요.

# 삼성 = Stock("삼성전자", "005930")

class Stock265:
    def __init__(self, st_name, st_code):
        self.st_name = st_name
        self.st_code = st_code
    def get_name(self):
        return self.st_name
    def get_code(self):
        return self.st_code

print("----- -----")
st265 = Stock265("삼성전자", "005930")
print(st265.get_code())
print(st265.get_name())
#  정답확인

# 266 객체의 속성값 업데이트
# 생성자에서 종목명, 종목코드, PER, PBR, 배당수익률을 입력 받을 수 있도록 생성자를 수정하세요. 
# PER, PBR, 배당수익률은 float 타입입니다.

class Stock266:
    def __init__(self, st_name, st_code, PER, PBR, beadang):
        self.st_name = st_name
        self.st_code = st_code
        self.PER = PER
        self.PBR= PBR
        self.beadang = beadang

#  정답확인

# 267 객체 생성
# 266번에서 정의한 생성자를 통해 다음 정보를 갖는 객체를 생성해보세요.

# 항목	    정보
# 종목명	삼성전자
# 종목코드	005930
# PER	    15.79
# PBR	    1.33
# 배당수익률 2.83
print("----- -----")
st = Stock266("삼성전자", "005930", 15.79, 1.33, 2.83)
print(st.PBR)
#  정답확인

# 268 객체의 속성 수정
# PER, PBR, 배당수익률은 변경될 수 있는 값입니다. 
# 이 값을 변경할 때 사용하는 set_per, set_pbr, set_dividend 메서드를 추가하세요.

class Stock268:
    def __init__(self, st_name, st_code, PER, PBR, dividend):
        self.st_name = st_name
        self.st_code = st_code
        self.PER = PER
        self.PBR = PBR
        self.dividend = dividend
    def set_per(self, PER):
        self.PER = PER
    def set_pbr(self, PBR):
        self.PBR = PBR
    def set_dividend(self, dividend):
        self.dividend = dividend

#  정답확인

# 269 객체의 속성 수정
# 267번에서 생성한 객체에 set_per 메서드를 호출하여 per 값을 12.75로 수정해보세요.

print("----- -----")
st = Stock268("삼성전자", "005930", 15.79, 1.33, 2.83)
print(st.PER)
st.set_per(12.75)
print(st.PER)
#  정답확인

# 270 여러 종목의 객체 생성
# 아래의 표를 참조하여 3종목에 대해 객체를 생성하고 이를 파이썬 리스트에 저장하세요. 
# 파이썬 리스트에 저장된 각 종목에 대해 for 루프를 통해 종목코드와 PER을 출력해보세요.

# 종목명	종목코드	PER	PBR	배당수익률
# 삼성전자	005930	15.79	1.33	2.83
# 현대차	005380	8.70	0.35	4.27
# LG전자	066570	317.34	0.69	1.37
print("----- -----")
lst = []
lst.append(st)
st2 = Stock268("현대차", "005380", 8.70, 0.35, 4.27)
st3 = Stock268("LG전자", "066570", 317.34, 0.69, 1.37)
lst.append(st2)
lst.append(st3)

for i in lst:
    print(i.st_code, i.PER)
#  정답확인
