# N, M = map(int, input().split())
# 이거 암기 !
N = 4
M = 2
lst = []
test1 = []
def dfs() :

    if len(lst) == M :
        #print(lst)
        print(' '.join(map(str, lst)))
        test1.append([lst[0], lst[1]])
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
test3 = list(map(tuple, test1))
print(test3)
#set(test3)
#print(test3)
'''
2차원 리스트를 set으로 변환해 중복 값을 제거하려고 하면 에러가 발생하는 경우가 있습니다.
        test2 = list( set(test1) )
    TypeError: unhashable type: 'list'
  
=> 이러한 경우에는 list 안에 있는 list를 tuple로 변환하고 set으로 다시 변환해 중복 값을 제거할 수 있습니다.

이 경우는 중복이 아닌 듯
(1,2) 와 (2,1) 은 다른 걸로

'''