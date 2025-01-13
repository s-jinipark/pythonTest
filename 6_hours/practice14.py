# import theater_module

# theater_module.price(3) # 3명이 영화 보러 갔을 때
# theater_module.price_morning(4)  # 4명이서 조조 할인 영화 보러 갔을 때
# theater_module.price_soldier(5)  # 5명의 군인이 영화 보러 갔을 때


# import theater_module as mv

# mv.price(3) # 3명이 영화 보러 갔을 때
# mv.price_morning(4)  # 4명이서 조조 할인 영화 보러 갔을 때
# mv.price_soldier(5)  # 5명의 군인이 영화 보러 갔을 때


# from theater_module import *

# price(3) # 3명이 영화 보러 갔을 때
# price_morning(4)  # 4명이서 조조 할인 영화 보러 갔을 때
# price_soldier(5)  # 5명의 군인이 영화 보러 갔을 때


from theater_module import price_soldier as ps
ps(5)

print("----------")
# 패키지
# import travel.thailand
# #import travel.thailand.ThailandPackage
# # -> 오류 남 : ModuleNotFoundError: No module named 'travel.thailand.ThailandPackage'; 'travel.thailand' is not a package
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()


# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()


# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# __all__
from travel import *
trip_to = vietnam.VietnamPackage()  #-> NameError: name 'vietnam' is not defined
# __init__.py 에 __all__ 에 vietnam 넣어 주면 오류 없이 실행됨
# trip_to = thailand.ThailandPackage() #-> 오류남
trip_to = thailand.ThailandPackage()  # -> __all__ 에 넣어 준 뒤
trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))
# thailand 를 random 있는 곳에 copy 하면 => random 있는 곳의 파일을 출력함


# pip install
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())


# 내장함수

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random # 외장 함수
# print(dir())
# import pickle
# print(dir())

# print(dir(random))

# lst = [1,2,3]
# print(dir(list))

# name = "Jim"
# print(dir(name))


# google 에서 "list of python builtins" 라고 입력 -> 검색


# 외장 함수
# google 에서 "list of python modules" 라고 입력 -> 검색

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob("*.py")) # 확장자가 py 인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd())

folder = "sample_dir"
if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder) # 폴더 생성
    print(folder, "폴더를 생성하였습니다.")

print(os.listdir())


# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은 ", today + td) # 오늘부터 100일 후
