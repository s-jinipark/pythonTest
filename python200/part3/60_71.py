'''
060 사용자 입력받기(input)
061 자료형 확인하기(type)
062 나눗셈에서 나머지만 구하기(%)
063 몫과 나머지 구하기(divmod)
064 10진수를 16진수로 변환하기(hex)
065 10진수를 2진수로 변환하기(bin)
066 2진수, 16진수를 10진수로 변환하기(int)
067 절대값 구하기(abs)
068 반올림수 구하기(round)
069 실수형 자료를 정수형 자료로 변환하기(int)
070 정수형 자료를 실수형 자료로 변환하기(float)
071 정수 리스트에서 소수만 걸러내기(filter)
'''

##################################################
print("060 사용자 입력받기(input)")
#k = input('<값>을 입력하세요')
#print('당신이 일력한 값은 '+ k + '입니다.')


##################################################
print("-----------------------------------")
print("061 자료형 확인하기(type)")

numdata = 57
strdata = '파이썬'
listdata = [1,2,3]
dicdata = {'a':1, 'b':2}

def func() :
    print('안녕하세요')

print(type(numdata))  # <class 'int'>
print(type(strdata))  # <class 'str'>
print(type(listdata)) # <class 'list'>
print(type(dicdata))  # <class 'dict'>
print(type(func))    # <class 'function'>


##################################################
print("-----------------------------------")
print("062 나눗셈에서 나머지만 구하기(%)")

a = 11113
b = 23
ret = a % b
print('%d  를 %d 로 나누면 %d 가 남습니다.'%(a,b,ret))


##################################################
print("-----------------------------------")
print("063 몫과 나머지 구하기(divmod)")
a = 11113
b = 23
ret1, ret2 = divmod(a, b)
print('%d / %d 는 몫이 %d 나머지가 %d 입니다.'%(a,b,ret1, ret2))


##################################################
print("-----------------------------------")
print("064 10진수를 16진수로 변환하기(hex)")
h1 = hex(97)    # 0x61
h2 = hex(98)    # 0x62 (문자열로 리턴됨)
ret1 = h1 + h2  # 0x610x62 가 출력
print(ret1)
a = int(h1, 16)
b = int(h2, 16)
#print(a)  #97
ret2 = a + b    # 10진수 195 가 됨
print(hex(ret2))  # '0xc3' 출력

##################################################
print("-----------------------------------")
print("065 10진수를 2진수로 변환하기(bin)")
b1 = bin(97)
b2 = bin(98)
ret1 = b1 + b2   # 0b11000010b1100010 가 출력
print(ret1)
a = int(b1, 2)
b = int(b2, 2)
ret2 = a + b     # 10진수 195 가 됨
print(bin(ret2)) # 0b11000011


##################################################
print("-----------------------------------")
print("066 2진수, 16진수를 10진수로 변환하기(int)")

bnum = 0b11110000; bstr = '0b11110000'
onum = 0o360; ostr = '0o360'
hnum = 0xf0; hstr = '0xf0'

b1 = int(bnum); b2 = int(bstr,2)   # b2 = int(bstr,0) 로도 가능
o1 = int(onum); o2 = int(ostr, 8)  # o2 = int(ostr, 0)
h1 = int(hnum); h2 = int(hstr, 16) # h2 = int(hnum, 0)

print(b1); print(b2)
print(o1); print(o2)
print(h1); print(h2)


##################################################
print("-----------------------------------")
print("067 절대값 구하기(abs)")
abs1 = abs(-3)
abs2 = abs(-5.72)
abs3 = abs(3+4j) # 복소수의 절대값
print(abs1)   # 3
print(abs2)   # 5.72
print(abs3)   # 5.0


##################################################
print("-----------------------------------")
print("068 반올림수 구하기(round)")
ret1 = round(1118)
ret2 = round(16.554)    # 소수점 첫째에서 반올림 (defalut : 0)
ret3 = round(1118, -1)  # 1의 자리에서 반올림
ret4 = round(16.554, 2) # 소수점 셋째자리에서 반올림
print(ret1)  # 1118
print(ret2)  # 17
print(ret3)  # 1120
print(ret4)  # 16.55


print("-----------------------------------")
print("069 실수형 자료를 정수형 자료로 변환하기(int)")
idata1 = int(-5.4)
idata2 = int(1.78e1)
idata3 = int(171.56)

print(idata1)  # -5
print(idata2)  # 17
print(idata3)  # 171


print("-----------------------------------")
print("070 정수형 자료를 실수형 자료로 변환하기(float)")
fdata = float(10)
print(fdata)


print("-----------------------------------")
print("071 정수 리스트에서 소수만 걸러내기(filter)")
def getPrime(x) :
    if x % 2 == 0 :
        return

    for i in range(3, int(x/2), 2):
        if x % i == 0 :
            break
    else :
        return x

listdate = [117,119,1113,11113,11119]
ret = filter(getPrime, listdate)
print(list(ret))
#print(ret)  # <filter object at 0x000001A68E4AEF88>

'''
파이썬 내장함수 filter() 는 리스트와 같이 반복 가능한 자료에서 특정 조건을 만족하는 값만을 
편리하게 추출할 수 있는 방법을 제공

(참고 013)
for 변수 in 범위:
   반복 실행 코드
else :
   for 구문이 모두 실행되었을 때 실행할 코드
 
'''

print("-----------------------------------")
print(" 정수 n  이하의 모든 소수 구하기")
def getPrime(n):
    ret = [2]
    if n <= 2 :
        return ret

    for i in range(3, n+1, 2) :
        for k in range(3, int(i/2), 2) :  # ???
            a = i % k
            if a == 0 :
                break
        else :
            ret.append(i)
    return ret

ret = getPrime(10)
print(ret)