
##### 중복순열 구하기

from itertools import product

def solution():
    answer = 0
    '''
    예시) 1,2,3,4,5가 적혀 있는 숫자 카드가 있다. 이를 중복을 허용해 세 자리 수를 만들 수 있는 방법은?
    
    중복허용 -> 중복 순열 ? => product

    '''
    test = [1,2,3]  # 구슬 3
    data = product(test, repeat=2)

    print(data)
    print(list(data))
    return answer

N = 3  # 구슬 1부터 3
M = 2  # M번 뽑는다
res = [0] * M  # 뽑은 구슬 번호 저장

re = solution()
print(re)
#=>
print('====================')

##### 여기서 정리
'''
[Python] 순열, 조합, 중복순열, 중복조합(itertools를 활용한 구현)
https://velog.io/@falling_star3/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%88%9C%EC%97%B4-%EC%A1%B0%ED%95%A9-%EC%A4%91%EB%B3%B5%EC%88%9C%EC%97%B4-%EC%A4%91%EB%B3%B5%EC%A1%B0%ED%95%A9itertools%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%9C-%EA%B5%AC%ED%98%84
 
'''
###✏ 순열(Permutation)
###👉🏻 순열은 순서를 고려하여 뽑는 경우의 수다.

'''
예시) 1,2,3,4,5가 적혀 있는 숫자 카드가 있다. 이를 이용해 세 자리 수를 만들 수 있는 방법은?

백의 자리에 올 수 있는 경우의 수: 5
십의 자리에 올 수 있는 경우의 수: 4
일의 자리에 올 수 있는 경우의 수: 3

백의 자리에 1이 올 때, 십의 자리에 올 수 있는 경우의 수는 2,3,4,5로 4가지이다. 
이는 백의 자리에 2,3,4,5가 올 때도 동일하다. 따라서 이는 5x4x3으로 곱의 법칙이 된다.

결론적으로, 서로 다른 숫자 5개 중에서 3개를 택하여 일렬로 배열한 경우의 수로
5P3 = 5x4x3 = 60
'''

from itertools import permutations

test1 = [1,2,3]
data1 = permutations(test1, 2)
print('permutations:', list(data1))


###✏ 조합(combination)
###👉🏻 조합은 순서를 생각하지 않고 뽑는 경우의 수다.

'''
예시) A,B,C,D,E 5명의 후보가 있다. 이 중 2명의 대표를 뽑는 방법은?

(A,B),(A,C),(A,D),(A,E)
(B,C),(B,D),(B,E)
(C,D),(C,E)
(D,E)

조합은 순서를 생각하지 않으므로 (A,B)와 (B,A)를 같은 것으로 본다.
즉, 순열은 5P2 = 5x4 = 20이지만 조합은 (5x5)/2 = 10 이다.

5C2 = 5P2/(2x1) = (5x4)/(2x1) = 10
'''

from itertools import combinations

test2 = ['A', 'B', 'C']
data2 = combinations(test2, 2)
print('combinations:', list(data2))


###✏ 중복순열(Permutation with repetition)
###👉🏻 중복순열은 순열과는 다르게 같은 숫자를 중복하여 사용할 수 있다.

'''
예시) 1,2,3,4,5가 적혀 있는 숫자 카드가 있다. 이를 중복을 허용해 세 자리 수를 만들 수 있는 방법은?

백의 자리에 올 수 있는 경우의 수: 5
십의 자리에 올 수 있는 경우의 수: 5
일의 자리에 올 수 있는 경우의 수: 5

백의 자리에 1이 올 때, 십의 자리에 올 수 있는 경우의 수는 1,2,3,4,5로 5가지이다. 
이는 백의 자리에 2,3,4,5가 올 때도 동일하다. 따라서 이는 5x5x5로 5^3이 된다.

결론적으로, 서로 다른 숫자 5개 중에서 중복을 허용해 3개를 택하여 일렬로 배열한 경우의 수로
5π3 = 5x5x5 = 125
'''

#from itertools import product

test3 = [1,2,3]
data3 = product(test3, repeat=2)
print('product:', list(data3))


###✏ 중복조합(Combination with repetition)
###👉🏻 중복조합은 조합과는 다르게 같은 숫자를 중복하여 사용할 수 있다.

'''
예시) A,B,C,D,E 5명의 후보가 있다. 이를 중복을 허용해 2명의 대표를 뽑는 방법은?

(A, A), (A, B), (A, C), (A, D), (A, E)
(B, B), (B, C), (B, D), (B, E)
(C, C), (C, D), (C, E)
(D, D), (D, E)
(E, E)

조합은 순서를 생각하지 않으므로 (A,B)와 (B,A)를 같은 것으로 본다. 
이 중 중복이 가능하니 (A,A)로 한 명이 대표직 2개를 겸할 수 있다.
6C2 = 6P2/r! = (6x5)/(2x1) = 15

'''

from itertools import combinations_with_replacement

test4 = ['A', 'B', 'C']
data4 = combinations_with_replacement(test4, 2)
print('combinations_with_replacement:', list(data4))
