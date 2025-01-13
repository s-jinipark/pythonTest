
# 데코레이터
# 이미 작성된 코드에 새로운 기능을 추가하여 함수 기능을 확장시키는 개념
# 
# 파이썬에서 함수는 일급 객체
# 클로저 사용
# 함수 내 함수를 정의할 수 있음
#  

def outer_function(msg):
    def inner_function():
        return  "내부 {} 메세지".format(msg)
    return inner_function

c = outer_function("헬로")
#print(c()) 
print(dir(c))
print(type(c.__closure__))


import time

def time_checker(func):
    def inner_function(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("함수 {} 동작시간 : {} ".format(func.__name__, end_time-start_time))
        return result
    return inner_function 

@time_checker
def test1():
    for i in range(5):
        time.sleep(0.1)

@time_checker
def test2():
    for i in range(10):
        time.sleep(0.1)

test1()
test2()

# def test():
#     start_time = time.time()
#     for i in range(5):
#         time.sleep(0.1)
#     end_time = time.time() - start_time
#     print("함수 동작 시간 : {}".format(end_time))
