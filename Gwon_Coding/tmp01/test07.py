# N, M = map(int, input().split())
# 이거 암기 !
N = 3
M = 3
lst = []
test1 = []
def dfs() :

    if len(lst) == M :
        #print(lst)
        print(' '.join(map(str, lst)))
        #test1.append([lst[0], lst[1]])
        return
    else :
        for i in range(1, N+1) :
            #if i not in lst :
            lst.append(i)
            dfs()
            lst.pop()

dfs()
print(test1)
#test2 = list( set(test1) )
#print(test2)
