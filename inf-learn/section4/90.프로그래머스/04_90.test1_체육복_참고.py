
# 프로그래머스 스타일 로 ...
def solution(n, lost, reserve):
    answer = 0
    # 전처리를 해준다며,
    set_reserve = set(reserve) - set(lost)
    print(set_reserve)
    set_lost =  set(lost) - set(reserve)
    print(set_lost)

    for i in set_reserve: # 체육복을 빌려줄수 있고
        if i-1 in set_lost : # 왼쪽요소(앞사람) 우선
            set_lost.remove(i-1)
        elif i+1 in set_lost :
            set_lost.remove(i+1)
    answer = n - len(set_lost)

    return answer

n = 5   # 전체 학생의 수

lost = [2,4]
reserve = [1,3,5]

re = solution(n, lost, reserve)
print('re :', re)
#=>
print('==============================')

n = 5   # 전체 학생의 수

lost = [2,4]
reserve = [3]

re = solution(n, lost, reserve)
print('re :', re)
#=>
print('==============================')

n =3

lost = [3]
reserve = [1]

re = solution(n, lost, reserve)
print('re :', re)
#=>
print('==============================')

n =5

lost = [4,5]
reserve = [3,4]

re = solution(n, lost, reserve)
print('re :', re)
#=> 4
print('==============================')