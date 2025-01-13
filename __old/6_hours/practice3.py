sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요."
print(sentence2)

sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

print("----------")
# 슬라이싱
jumin = "990120-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 부터 2 직전까지
print("월 : " + jumin[2:4]) # 2 부터 4 직전까지
print("일 : " + jumin[4:6]) # 4 부터 6 직전까지

print("생년월일 : " + jumin[:6]) 
print("뒤 7자리 : " + jumin[7:]) 
print("뒤 7자리 (뒤에서부터): " + jumin[-7:]) 

print("----------")
# 문자열 처리함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index+1) # 두번째 n
print(index)

print(python.find("Java")) # -1
#print(python.index("Java")) # ValueError: substring not found

print(python.count("n"))

print("----------")
# 문자열 포맷
print("나는 %d 살입니다." % 20)
print("나는 %s 를 좋아해요." % "파이썬")
print("Apple 은 %c 로 시작해요." % "A")

# %s
print("나는 %s 살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파랑", "빨강"))

# 방법2
print("나는 {} 살입니다.".format(20) )
print("나는 {} 색과 {} 색을 좋아해요.".format("파랑", "빨강"))
print("나는 {0} 색과 {1} 색을 좋아해요.".format("파랑", "빨강"))
print("나는 {1} 색과 {0} 색을 좋아해요.".format("파랑", "빨강"))

# 방법3
print("나는 {age} 살이며,  {color} 색을 좋아해요.".format(age= 20, color= "빨강"))

# 방법4 (v3.6 이상)
age = 20
color = "빨강"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

print("----------")
# 탈출 문자
# \n : 줄바끔
print("백문이 불여일견 \n백견이 불여일타")

# \" \' : 문장 내에서 따옴표
# 저는 "나도코딩"입니다.
print("저는 '나도코딩' 입니다.")
print('저는 "나도코딩" 입니다.')
print("저는 \"나도코딩\" 입니다.")
print("저는 \'나도코딩\' 입니다.")

# \\ : 문장내에서 \
#print("C:\Users\jini\Desktop") 
#-> SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

print("C:\\Users\\jini\\Desktop") 


# \r : 커서를 맨 앞으로 이동
print("Read Apple \rPine")  #-> Pine Apple

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")