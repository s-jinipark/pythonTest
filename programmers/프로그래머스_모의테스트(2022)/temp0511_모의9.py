# 다음과 같이 import를 사용할 수 있습니다.
# import math
from  itertools  import combinations

def solution(arr, K):
    # 여기에 코드를 작성해주세요.
    answer = 9999

    #[*3] 마지막에 이거 넣어 줌
    arr.sort()

    lst = (list)(combinations(arr, K))

    for l in lst:

        # 연습 = max(l)-min(l)
        # print(l, 연습)
        # if answer > 연습:
        #     answer = 연습
        # -> 시간 초과 나옴

        # 연습 = (list) (l)
        # #print(연습)
        # 연습.sort()
        # print(연습, 연습[0], 연습[-1])
        # diff = 연습[-1] - 연습[0]
        # if answer > diff:
        #     answer = diff
        # -> (마찬가지) 시간 초과 나옴

        # diff = l[-1] - l[0]
        # if answer > diff:
        #     answer = diff
        # -> (마찬가지) 시간 초과 나옴

        print(l)

    for i in range(0, len(arr) - K + 1):
        print(i + K - 1, i, '>', arr[i + K - 1] , arr[i])
        answer = min(answer, arr[i + K - 1] - arr[i])

    #print(lst)

    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [9, 11, 9, 6, 4, 19]
K = 4
ret = solution(arr, K)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")