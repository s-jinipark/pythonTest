def solution(id_list, report, k):
    answer = []
    dict = {}
    dict2 = {}
    dict3 = {}
    for i in id_list:
        dict[i] =[]
        dict2[i] = 0
        dict3[i] = 0
    print(dict)

    for r in report:
        From, To = r.split()
        #print(From, To)
        if To not in dict[From] :  # ** 2nd 여러번 신고는 한번으로 처리
            dict[From].append(To)
            dict2[To] += 1
    print(dict)
    print(dict2)
    print(dict3)

    # k 번 이상인 사람
    for d in dict2:
        #print(dict2[d])
        if dict2[d] >= k :
            print(d) # => 신고 당한 사람
            # 이들을 신고한 사람들
            for dd in dict:
                print(dict[dd])
                if d in dict[dd] :
                    print ('>', dd)
                    # 메일을 보냄
                    dict3[dd] += 1
    print(dict3)

    for i in dict3:
        answer.append(dict3[i])
    return answer

# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 2

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

re = solution(id_list, report, k)
print(re)

print("====================")

