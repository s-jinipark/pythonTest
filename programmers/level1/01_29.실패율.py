def solution(N, stages):
    answer = []
    dict = {}
    for i in range(1, N+1):
        #print(i)
        tmp_cnt = 0
        tmp_tot = 0
        for j in range(len(stages)):
            if i == stages[j] :
                tmp_cnt += 1
            if i <= stages[j] :
                tmp_tot += 1
        #print(i, tmp_cnt/tmp_tot)
        if tmp_tot == 0 :
            dict[i] = 0
            continue
        dict[i] = tmp_cnt/tmp_tot
    print(dict)
    new_dict = sorted(dict.items(), key=lambda  x : x[1] , reverse=True)
    print(new_dict)
    for i in new_dict:
        print(i[0])
        answer.append(i[0])
    return answer

N = 5
#stages = [2, 1, 2, 6, 2, 4, 3, 3]
stages = [2, 1, 2, 1, 2, 4, 3, 3]

re = solution(N, stages)
print(re)

'''
계산 값은 산출 했으나, 이중 sort 가 문제

dict + lam

score_dict = {
    'sam':23,
    'john':30,
    'mathew':29,
    'riti':27,
    'aadi':31,
    'sachin':28
}
dict 의 스코어대로 정렬하는 방법입니다.

    new_dict = sorted(score_dict.items(), key=lambda x:x[1], reverse=True)
    print(new_dict)
    # [('aadi', 31), ('john', 30), ('mathew', 29), ('sachin', 28), ('riti', 27), ('sam', 23)]

스코어빼고 이름만 정렬하고 싶다면,

    new_dict = sorted(score_dict, key=lambda x: score_dict[x], reverse=True)
    print(new_dict)
    # ['aadi', 'john', 'mathew', 'sachin', 'riti', 'sam']
    sorted 의 첫번째 파라메터를 score_dict.items() 에서 score_dict 로 바꾸면 되네요.
    key 에서 x 는 dict 의 key가 됩니다. 점수로 정렬을 하려면 score_dict[key] 가 되어야 하기때문에 score_dict[x] 로 했습니다.

'''

print("====================")

