from itertools import combinations
from itertools import combinations_with_replacement

def rtn_order(want, ptable):
    for i in range(len(ptable)):
        #print(i, ptable[i])
        if want == ptable[i] :
            return i+1


def solution(pricetable, budget):
    answer = []
    lst =  []
    # 중복 허용 뽑기를 해야 하는데...

    #c = combinations(pricetable, 3)
    #print(list(c))
    # [(1000, 3000, 2500), (1000, 3000, 1500), (1000, 2500, 1500), (3000, 2500, 1500)]

    cb2 = combinations_with_replacement(pricetable, 3)
    #print(list(cb2))
    #print(type(cb2))
    lst2 = list(cb2)
    print(type(lst2))
    print(lst2)
    for c in lst2 :
        #print(c)
        tmp = c[0] + c[1] + c[2]
        if c[0] == c[1] or c[1] == c[2] :
            tmp -= c[1]
        elif c[2] == c[0]:
            tmp -= c[0]

        if tmp == budget:
            print(c)
            tmp_lst = []
            tmp_lst.append(rtn_order(c[0], pricetable))
            tmp_lst.append(rtn_order(c[1], pricetable))
            tmp_lst.append(rtn_order(c[2], pricetable))
            tmp_lst.sort()
            answer.append(tmp_lst)
    return answer

pricetable   = [1000, 3000, 2500, 1500]
budget = 5000
res = solution(pricetable, budget)
print(res)


pricetable   = [1000, 3000, 2500, 1500, 2500, 1500]
budget = 4500
res = solution(pricetable, budget)
print(res)