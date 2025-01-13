print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

print('풍선')
print("나비")
print("ㅋ"*9)

# 참 / 거짓
print(5 >10)
print(5 <10)
print(True)
print(not True) # False
print(not (5>10)) # True

# 애완동물을 소개해 주세요
animal = "고양이" #"강아지"
name = "연탄이"
age = 4
is_adult = age >=3

print("우리집 " + animal +"의 이름은 " + name + "이예요")
print(name + "는 " +str(age) + " 살이며, 산책을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult) )
# str 없으면 : TypeError: can only concatenate str (not "bool") to str

print(name, "는" , age,  "살이며, 산책을 아주 좋아해요")
#-> , 를 쓰면 str() 없이 정수형 사용 가능, 공백이 한칸씩 추가됨

''' 
여러문자 주석처리
이거다
'''