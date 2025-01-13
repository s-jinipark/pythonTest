
# 표준입출력
print("Python", "Java", sep=",", end="?")
print("무엇이 더 재미있을까요?")

import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

# 시험 성적
score = {"수학":0, "영어":50, "코딩":100}
for subject, score in score.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순법표
# 001, 002, 003, ...

for num in range(1, 21):
    #print("대기번호 : " + num) #->TypeError: can only concatenate str (not "int") to str
    #print("대기번호 : " + str(num)) 
    print("대기번호 : " + str(num).zfill(3)) 

# 표준 입력
# answer = input("아무 값이나 입력하세요 : ")
# print(type(answer))  #-> <class 'str'>
# print("입력하신 값은 " + answer + " 입니다. ")

# answer =10 
# print(type(answer))  #-> <class 'int'>

print("----------")
# 다양한 출력 포맷

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일 땐 + 로 표시, 홀수일 땐 - 로 표시
print("{0: >+10}".format(500))
print("{0: >-10}".format(-500))

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))
print("{0:_<10}".format(500))

# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000000))

# 3자리 마다 콤마를 찍어주기, +-부호도 붙이기
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))

# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자리수 확보하기
# 돈이 많으면 행복하니까 빈 자리는 ^ 로 채워주기
print("{0:^<+30,}".format(100000000000))

# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수 까지만 출력(소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))

print("----------")
# 파일 입출력
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") # append
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) # 줄별로 읽기
# print(score_file.readline())
# print(score_file.readline(), end="") # 줄바꿈을 하지 않겠다.
# print(score_file.readline(), end="")
# score_file.close()

# 파일이 총 몇줄인지 모를 경우
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()


score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()

print("----------")
# pickle
import pickle
profile_file = open("profile.pickle", "wb") # b 는 binary
profile = {"이름":"박명수", "나이":"50", "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file 에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()

print("----------")
# with

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
# 수월하게 파일에 대한 처리, close 도 없고...

