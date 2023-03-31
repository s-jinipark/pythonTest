

inp = '2143'
lst = []

for i in inp :
    lst.append(int(i))

print(lst)

'''
선택 정렬
대상 데이터에서 최대나 최소 데이터를 데이터가 나열된 순으로 찾아가며 선택하는 방법
구현이 복잡하고, 시간 복잡도도 효율적이지 않아 코딩 테스트에서는 많이 사용하지 않음

(핵심)
최솟값 또는 최댓값을 찾고,
남은 정렬 부분의 가장 앞에 있는 데이터와 swap 하는 것이 선택 정렬의 핵심

[my]
이건 앞에서 부터 채워나감
겉의 i 가 증가하면서 하나씩
 안의 j 에서 max 찾아서 i 와 교체
'''
for i in range(len(lst)) :
    Max = i  # [ <- 여기서 인덱스를 넣는다는 점]
    for j in range(i+1, len(lst)) :
        if lst[j] > lst[Max] :  # [ <- 실제 값 비교]
            Max = j  # [<- 다시 인덱스 업데이트, 흠 좀 헷갈리는 군]
    if lst[i] < lst[Max] :
        tmp = lst[i]
        lst[i] = lst[Max]
        lst[Max] = tmp

print(lst)
