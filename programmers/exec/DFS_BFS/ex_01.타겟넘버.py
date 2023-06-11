
def DFS(v, sum):
    global  cnt
    #if v == len_num-1 :
    # [2]
    if v == len_num :

        #print(sum)
        if sum == target :
            cnt += 1
        return
    else :
        #DFS(v + 1, sum + ( numbers[v + 1] ))
        #DFS(v + 1, sum + ( numbers[v + 1] * -1))
        # [2] -1 을 0 으로 관련
        DFS(v + 1, sum +  numbers[v] )
        DFS(v + 1, sum -  numbers[v] )

def solution(numbers, target):
    answer = 0

    #DFS(-1, 0)
    # [2] 하다보니 -1 로 적었는데, 다시 0 으로, 답은 맞게 나옴
    DFS(0, 0)

    return answer

numbers	= [1, 1, 1, 1, 1]
target = 3
# return = 5
len_num = len(numbers)
cnt = 0

re = solution(numbers, target)
print(re)
print('cnt:', cnt)
