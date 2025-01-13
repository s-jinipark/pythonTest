def solution(i1, i2):
    answer = 0

    ilist1 = i1.split()
    print(ilist1)
    tmp_max = []

    for i in range(int(ilist1[0]) ):
        #print(i2[i])
        ilist2 = i2[i].split()
        tmp_min = 10000
        for j in range(int(ilist1[1]) ):
            #print(ilist2[j] )
            if tmp_min > int(ilist2[j] ) :
                tmp_min =  int(ilist2[j])
        tmp_max.append(tmp_min)
    #print(tmp_max)
    # 이중 가장 큰 것
    answer = 0
    for k in tmp_max :
        if answer < k :
            answer = k
    return answer

def example(i1, i2):
    answer = 0

    ilist1 = i1.split()
    print(ilist1)

    result = 0
    for i in range(int(ilist1[0])) :
        data = i2[i].split()
        # 가장 작은 수 찾기
        min_value = min(data)
        #print(min_value)
        # 가장 작은 수 중에서 가장 큰 수 찾기
        result = max(result, int(min_value) )

    return result

inp1 = "3 3"
inp2 = ["3 1 2", "4 1 4", "2 2 2"]

print("----- -----")
print(solution(inp1, inp2))
print(example(inp1, inp2))

inp1 = "2 4"
inp2 = ["7 3 1 8", "3 3 3 4"]

print("----- -----")
print(solution(inp1, inp2))