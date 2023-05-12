
def solution_bubble(tmplist):
    for i in range(len(tmplist)) :
        for j in range(len(tmplist)-1):
            if tmplist[j] > tmplist[j+1]:
                tmp = tmplist[j+1]
                tmplist[j + 1] = tmplist[j]
                tmplist[j] = tmp
        print(tmplist)

def solution_select(tmplist): # 선택정렬
    #최소값 선택
    for i in range(len(tmplist)):
        minidx = i
        for j in range(i+1, len(tmplist)):
            if tmplist[j] < tmplist[minidx] :
                minidx = j
        if minidx != i :
            tmp = tmplist[i]
            tmplist[i] = tmplist[minidx]
            tmplist[minidx] = tmp
        print(tmplist)

def solution_insert(tmplist): # 삽입정렬
    #타겟 숫자와 이전 원소 비교
    for i in range(1, len(tmplist)):
        bk = tmplist[i]
        idx = i -1
        while idx >= 0 and bk < tmplist[idx] :
            tmplist[idx+1] = tmplist[idx]
            idx -= 1 # 줄줄이 이동
        tmplist[idx+1] = bk
        print(tmplist)

print('정렬')
tmplist = [10, 2, 6, 4, 3, 7, 5]
print(tmplist)
print()
solution_bubble(tmplist)   # 버블 정렬

print()
tmplist = [10, 2, 6, 4, 3, 7, 5]
solution_insert(tmplist)   # 삽입 정렬

print()
tmplist = [10, 2, 6, 4, 3, 7, 5]
solution_select(tmplist)   # 선택 정렬

# extra - heapq

import heapq

def solution_heapq(arr):
    answer = 0
    heap = []

    # arr 다 집어 넣는다
    for i in arr :
        heapq.heappush(heap, i)

    # 반복을 하는데
    #1. PQ 2개 꺼내기(가장 작은 값이 나오게 됨)
    #2. 합성하고 만들어진 것 PQ 에 다시 넣기
    while len(heap) != 1 :
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        sum = a + b
        print(a, b)
        answer += sum
        heapq.heappush(heap, sum)

    return answer

arr = [1, 2, 3, 4, 5]
a = solution_heapq(arr)
print(a)
