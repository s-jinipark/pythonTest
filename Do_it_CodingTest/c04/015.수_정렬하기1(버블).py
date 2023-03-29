

N = 5
lst = [5,2,3,4,1]

#lst.sort()
print(lst)

'''
버블 정렬 
간단하게 구현할 순 있지만, 시간 복잡도는 O(n제곱)으로 
다른 정렬 알고리즘보다 속도가 느린 편 

[my]
for 문이 key
0 부터 N-1 까지 루핑
  j 도 0 부터 ? j 내에서 j 와 j+1 을 비교
바깥의 i 는 범위를 점점 좁히는 역할?
'''
for i in range(N-1):
    for j in range(N-1-i):

        if lst[j] > lst[j+1] :
            tmp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = tmp

        print(i, '>' , lst)

print(lst)

