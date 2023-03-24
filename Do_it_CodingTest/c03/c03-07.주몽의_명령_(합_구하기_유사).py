

'''
2개의 재로로 만든다..
2개의 합이 9 이면 된다

=> 연속된 자연수의 합 (응용?)
'''

n = 6  # 재료의 개수
m = 9  # 갑옷이 완성되는 번호의 합

lst = [ 2,7,4,1,5,3 ]

# 정렬
lst.sort()
print(lst)

count = 0
i = 0     # 시작 인덱스
j = n -1  # 종료 인덱스

while i < j :
    if lst[i] + lst[j] < m:
        i += 1
    elif lst[i] + lst[j] > m:
        j -= 1
    else :
        count += 1
        print(i, j)
        i += 1
        j -= 1
    '''
    if 재료 합 < M :  작은 번호 재료를 한 칸 위로 변경
    elif 재료 합 > M :  큰 번호 재료를 한 칸 아래로 변경
    else 경우의 수 증가, 양쪽 index 각각 변경(*)
    '''
print(count)
