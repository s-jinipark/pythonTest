

# ------------------------------
# n번째 원소까지
def solution1(num_list, n):
    answer = []
    for i in range(n):
        answer.append(num_list[i])
    return answer


num_list =[2, 1, 6]
n = 1

res = solution1(num_list, n)
print(res)


# ------------------------------
# 길이에 따른 연산
'''
정수가 담긴 리스트 num_list가 주어질 때, 리스트의 길이가 11 이상이면 리스트에 있는 모든 원소의 합을 
10 이하이면 모든 원소의 곱을 return하도록 solution 함수를 완성해주세요.
'''
def solution2(num_list):
    answer = 0
    len_lst = len(num_list)
    if len_lst >= 11 :
        answer = sum(num_list)
    else:
        answer = 1
        for i in range(len_lst):
            answer *= num_list[i]

    return answer


num_list =[3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]
result = 51

res = solution2(num_list)
print(res)


# ------------------------------
# 문자열의 앞의 n글자
def solution3(my_string, n):
    answer = ''
    print(my_string[:n])
    answer = my_string[:n]
    return answer


my_string ="ProgrammerS123"
n = 11

res = solution3(my_string, n)
print(res)


# ------------------------------
# 문자열의 뒤의 n글자
'''
문자열 my_string과 정수 n이 매개변수로 주어질 때, 
my_string의 뒤의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.
'''
def solution4(my_string, n):
    answer = ''
    len_str = len(my_string)
    print(my_string[-n:])
    answer = my_string[-n:]
    return answer


my_string ="ProgrammerS123"
n = 11

res = solution4(my_string, n)
print(res)


# ------------------------------
# 부분 문자열인지 확인하기
'''
부분 문자열이란 문자열에서 연속된 일부분에 해당하는 문자열을 의미합니다. 
예를 들어, 문자열 "ana", "ban", "anana", "banana", "n"는 모두 문자열 "banana"의 부분 문자열이지만, 
"aaa", "bnana", "wxyz"는 모두 "banana"의 부분 문자열이 아닙니다.
'''

# 부분 문자열이라면 1을, 아니라면 0을 return
def solution5(my_string, target):
    answer = 0
    if target in my_string:
        print(1)
        answer = 1
    #else:
    #    print(0)
    return answer


my_string ="banana"
target = 'wxyz'  #'ana'

res = solution5(my_string, target)
print(res)


# ------------------------------
# 공배수

# n의 배수이면서 m의 배수이면 1을 아니라면 0을 return
def solution6(number, n, m):
    answer = 0
    if number % n == 0 and number % m == 0 :
        answer = 1
    else:
        answer = 0

    return answer


number = 60
n = 2
m = 3

res = solution6(number, n, m)
print(res)


'''
TO-DO :

문자열 자르기

'''