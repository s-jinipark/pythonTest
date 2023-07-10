
# 씨름 선수(그리디)
def solution(n, inp):
    answer = 0

    # 키 순서 정렬을 하고, 체중이 높은사람이 있으면 탈락
    #inp.sort()
    # for i in range(n-1):
    #     #print(i)
    #     for j in range(i+1, n):
    #         print(i, j, inp[i][1], inp[j][1])
    #         if inp[i][1] < inp[j][1]:
    #             answer += 1
    #             break
    '''
    문제 -> 탈락자를 계산 함
    이 것도 문제지만..
    소팅을 내림차순으로 해야 함
      -> 그 다음 몸무게를 비교하는데, max 를 갱신하면 cnt 한다
    
    이중 for 문은 비 효율적이라며...  
    '''

    inp.sort(reverse=True)
    # 그 다음은 몸무게만 본다
    large = 0
    # for i in inp:
    #     print(i)
    #-> 이렇게 해도 되지만 tuple 값을 받으려고
    for x, y in inp:
        print(x, y)
        if y > large:
            answer +=1
            large = y
    return answer

'''
그리디는 대부분 정렬 문제임

문제를 잘 못 읽었음.. 탈락자를 cnt 했음
뽑히는 수를 계산해야 함

'''

n = 5

inp = [
    (172, 67),
    (183, 65),
    (180, 70),
    (170, 72),
    (181, 60)
]

re = solution(n, inp)
print('re :', re)
#=>
print('==============================')

