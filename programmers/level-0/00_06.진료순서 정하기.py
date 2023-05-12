def solution(emergency):
    answer = []
    copy_arr = [0] * len(emergency)
    rank_arr = [0] * len(emergency)
    #print(copy_arr)
    for i in range(len(emergency)) :
        copy_arr[i] = emergency[i]
    emergency.sort(reverse=True)
    print(copy_arr, emergency)
    # emergency 루프 돌면서, copy array 에서 위치를 받고
    # 값을 rank 에 넣는다
    for i in range(len(emergency)):
        #print(i)
        for j in range(len(copy_arr)):
            if emergency[i] == copy_arr[j] :
                print(j)
                rank_arr[j] = i+1
                break
    answer = rank_arr
    return answer

e = [3, 76, 24]

re = solution(e)

print(re)
print("====================")

