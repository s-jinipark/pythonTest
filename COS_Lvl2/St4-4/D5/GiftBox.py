from itertools import combinations

def solution(pricetable, budget):
    answer = []
    lst =  []
    # 중복 허용 뽑기를 해야 하는데...
    for i in range(len(pricetable)):
        for j in range(len(pricetable)):
            for k in range(len(pricetable)) :
                tmp = pricetable[i] +  pricetable[j] +  pricetable[k]
                if i == j or j == k :
                    tmp -= pricetable[j]
                elif  k == i :
                    tmp -= pricetable[k]

                if tmp == budget :
                    #print(i, j, k , 연습)
                    lst.append((i,j,k))
    print(lst)
    print(set(lst))
    return answer


pricetable   = [1000, 3000, 2500, 1500]
budget = 5000
res = solution(pricetable, budget)
print(res)


pricetable   = [1000, 3000, 2500, 1500, 2500, 1500]
budget = 4500
res = solution(pricetable, budget)
print(res)