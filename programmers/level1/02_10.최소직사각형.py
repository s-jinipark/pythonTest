def solution(sizes):
    answer = 0
    Min = 1000*1000
    #print(cal_size(sizes))
    max_0 = 0
    max_1 = 0

    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1] :
            change = 0
            change = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = change

        if max_0 < sizes[i][0]:
            max_0 = sizes[i][0]

        if max_1 < sizes[i][1]:
            max_1 = sizes[i][1]
        # tmp = cal_size(sizes)
        # print(tmp)
        # if Min > tmp:
        #     Min = tmp
    tmp = max_0 * max_1
    if Min > tmp:
        Min = tmp
    answer = Min
    return answer

def cal_size(s):
    max_0 = 0
    max_1 = 0
    for i in range(len(s)):
        print(s[i][0], s[i][1])
        if max_0 < s[i][0]:
            max_0 = s[i][0]
        if max_1 < s[i][1]:
            max_1 = s[i][1]
    return max_0 * max_1

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

re = solution(sizes)
print(re)


'''
[1st]
def solution(sizes):
    answer = 0
    Min = 1000*1000
    #print(cal_size(sizes))
    for i in range(len(sizes)):
        tmp = cal_size(sizes)
        print(tmp)
        change = 0
        change =  sizes[i][0]
        sizes[i][0] = sizes[i][1]
        sizes[i][1] = change
        tmp2 = cal_size(sizes)
        print(tmp2)
        if Min > tmp:
            Min = tmp
        if Min > tmp2:
            Min = tmp2
    answer = Min
    return answer

def cal_size(s):
    max_0 = 0
    max_1 = 0
    for i in range(len(s)):
        print(s[i][0], s[i][1])
        if max_0 < s[i][0]:
            max_0 = s[i][0]
        if max_1 < s[i][1]:
            max_1 = s[i][1]
    return max_0 * max_1

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

re = solution(sizes)
print(re)
'''
