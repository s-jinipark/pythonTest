
# 사용자 함수

# 호출을 해 주어야 실행됨
# def add(a, b):  # 괄호 안 : 매개변수, 파라메타, 파람, 인자값 등
#                 # 여러 단어로 표현됨
#     return a + b

# print(add(1,2))

#--------------------------------------------------
# c = 10
# def add(a, b):  
#     global c     # 전역 변수를 사용하겠다..
#     c = a + b
#     return c

# b = add (1, 10)
# print(b, c)

#--------------------------------------------------

# def get_input_user(msg, casting):
#     while True:
#         try:
#             user = casting(input(msg))
#             return user
#         except:
#             continue

# user = get_input_user("사용자 이름을 입력하세요> ", str)
# age = get_input_user("사용자 나이를 입력하세요> ", int)

#--------------------------------------------------

# def test1(num):
#     num += 10
#     print(num)

# def test2(lists):
#     lists.append("AAAA")
#     print(lists)

# a = 50
# test1(a) # 앞의 값과는 다름
# print(a) # immutable
# a = []
# a.append("1234")
# test2(a)  # List, Dictionary, Set 호출 전 에도 영향
# print(a)

#--------------------------------------------------

# def save_winner(*args):
#     print(args)
#     print(args[0])

# save_winner("홍길동")
# save_winner("홍길동", "가가멜")
# save_winner("홍길동", "가가멜", "아즈라엘")

# def save_winner2(**kwargs):    # keyword argument
#     print(kwargs)
#     if kwargs.get("name1"):
#         print(kwargs["name1"])

# save_winner2(name1="홍길동", naem2="가가멜")

#--------------------------------------------------

# def hi():
#     print("Hello")

# hello = hi
# hello()
# print(type(hello))

#--------------------------------------------------

# def add(a, b):
#     return a + b

# def cal(func, a, b):
#     print("결과 {}".format(func(a,b)))

# cal(add, 1, 5)


#--------------------------------------------------
# 함수 안에 함수 선언

def outer_function(func):
    def inner_function(*args, **kwargs):
        print("함수명 : {}".format(func.__name__))
        print("args : {}".format(args))
        print("kwargs : {}".format(kwargs))
        result = func(*args, **kwargs)
        print("result : {}".format(result))
        return result
    return inner_function

def add(a, b):
    return a + b

f = outer_function(add)
f(10,20)

# 데코레이션 할 때 한번 더..

