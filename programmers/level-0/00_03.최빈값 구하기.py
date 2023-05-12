def solution(array):
    answer = 0
    dict = {}
    for a in array:
        if a in dict:
            dict[a] += 1
        else :
            dict[a] = 1
    #print(max(dict.values()))
    Max = max(dict.values())
    cnt = 0
    max_idx = 0
    for i in dict.keys() :
        print(dict[i])
        if dict[i] == Max :
            cnt +=1
            max_idx = i
    if cnt > 1 :
        answer = -1
    else :
        answer = max_idx
    return answer

#a = [1, 2, 3, 3, 3, 4]
#a = [1, 1, 2, 2]
a = [1,1,2,3]
re = solution(a)

print(re)
print("====================")

