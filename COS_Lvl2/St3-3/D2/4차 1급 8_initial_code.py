# 다음과 같이 import를 사용할 수 있습니다.
# import math
import itertools

def solution(card, n):
    # 여기에 코드를 작성해주세요.
    answer = 0
    # 4개의 숫자를 이용해 배열..
    """
    itertools.permutation를 이용하면, for문을 사용하지 않고도
    순열을 구할 수 있습니다.

    import itertools

    pool = ['A', 'B', 'C']
    print(list(map(''.join, itertools.permutations(pool))))  # 3개의 원소로 수열 만들기
    print(list(map(''.join, itertools.permutations(pool, 2))))  # 2개의 원소로 수열 만들기
    """
    #print(list(itertools.permutations(card, len(card) ) ))
    #print(list(map( ''.join, itertools.permutations(card, len(card)))))
    #=>TypeError: sequence item 0: expected str instance, int found
    card_count = list(itertools.permutations(card, len(card)))
    card_num = []
    #print(card_count)
    for v in card_count:
        #card_num.append(  ''.join(map(str, v)))
        #-> ['1213', '1231', ...
        card_num.append( int(''.join(map(str, v))) )
        #=> [1213, 1231, ...

    print(card_num)
    card_num = list(set(card_num))  # 동일 제거 ?
    card_num.sort()
    print(card_num)

    if n not in card_num :
        return -1

    answer = card_num.index(n) + 1

    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
card1 = [1, 2, 1, 3]
n1 = 1312
ret1 = solution(card1, n1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
card2 = [1, 1, 1, 2]
n2 = 1122
ret2 = solution(card2, n2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")