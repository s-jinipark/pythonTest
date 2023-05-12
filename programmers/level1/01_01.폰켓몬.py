def solution(nums):
    answer = 0
    dict = {}
    for n in nums:
        if n in dict :
            dict[n] += 1
        else :
            dict[n] = 1
    #print(len(dict))
    #print(int(len(nums)/2))
    len_dict = len(dict)
    len_nums2 = int(len(nums)/2)
    if len_dict >= len_nums2:
        answer = len_nums2
    else :
        answer = len_dict
    return answer


#inp = [3,1,2,3]
inp = [3,3,3,2,2,4]
re = solution(inp)
print(re)

print("====================")
# set 으로 다시 한 번
def solution2(nums):
    answer = 0
    tmp_set = set(nums)
    print(tmp_set)

    return answer

re2 = solution2(inp)
print(re2)
