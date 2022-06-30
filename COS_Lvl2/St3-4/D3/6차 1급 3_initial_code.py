#다음과 같이 import를 사용할 수 있습니다.
#import math
from itertools import combinations

def solution(arr, K):
    #여기에 코드를 작성해주세요.
    answer = 0
    combi = list(combinations(arr, K))
    #print(combi)
    answer = 9999
    for c in combi :
        #print(c)
        min_tmp = min(c)
        max_tmp = max(c)
        #print(min_tmp, max_tmp)
        if (max_tmp - min_tmp) < answer :
            answer = (max_tmp - min_tmp)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [9, 11, 9, 6, 4, 19]
K = 4
ret = solution(arr, K)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")


'''
순열(Permutations)

from itertools import combinations, permutations

nums = [1,2,3,4]
perm = list(combinations(nums, 2))
[(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)] 출력


조합(Combinations)

from itertools import combinations, permutations

nums = [1,2,3,4]
combi = list(combinations(nums, 2))
[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)] 출력
'''