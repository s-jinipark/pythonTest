

N = 5
lst = [5,2,3,4,1]

#lst.sort()
print(lst)

'''
for 문이 key
0 부터 N-1 까지 루핑
  j 도 0 부터 ? j 내에서 j 와 j+1 을 비교
바깥의 i 는 범위를 점점 좁히는 역할?
'''
for i in range(N-1):
    for j in range(N-1-i):
        print('>' , lst)
        if lst[j] > lst[j+1] :
            tmp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = tmp

print(lst)

