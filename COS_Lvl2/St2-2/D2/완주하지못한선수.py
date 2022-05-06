# 완주하지못한선수

def solution(participant, completion):
    answer = ''

    part_dict = {}
    for p in participant :
        if p in part_dict :
            part_dict[p] += 1
        else :
            part_dict[p] = 1
    print(part_dict)

    for c in  completion :
        if c in part_dict :
            part_dict[c] -= 1
    print(part_dict)

    for p in part_dict :
        if part_dict[p] > 0 :
            answer = p
    return answer


# main 부분
participant = ['leo', 'kiki', 'eden']
completion = ['eden', 'kiki']     # 'leo'
res = solution(participant, completion)
print(res)

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]       # "vinko"
res = solution(participant, completion)
print(res)

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]                   # "mislav"
res = solution(participant, completion)
print(res)

