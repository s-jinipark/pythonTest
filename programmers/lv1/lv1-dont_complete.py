
# 완주하지 못한 선수

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    print(participant)
    print(completion)
    print(len(participant))
    for i in range(0, len(completion)):
        #print(participant[i])
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    # 다른게 없을 경우
    if answer == '':
        answer = participant[len(participant)-1]

    return answer

# p1 = ["leo", "kiki", "eden"]
# c1 = ["eden", "kiki"]
# an1 = solution(p1, c1)
# print(an1)

# p1 = ["marina", "josipa", "nikola", "vinko", "filipa"]
# c1 = ["josipa", "filipa", "marina", "nikola"]
# an1 = solution(p1, c1)
# print(an1)

p1 = ["mislav", "stanko", "mislav", "ana"]
c1 = ["stanko", "ana", "mislav"]
an1 = solution(p1, c1)
print(an1)
