
# 프로그래머스 스타일 로 ...
def solution(inA, inB):
    answer = 0

    tmp = inA + inB
    print(tmp)
    tmp.sort()
    print(tmp)
    return answer


inA = [1,3,5]
inB = [2,3,6,7,9]
re = solution(inA, inB)
print(re)
#=>
print('==============================')
