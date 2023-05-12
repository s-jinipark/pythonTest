def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    print(participant)
    print(completion)
    for i in range(len(completion)):  # 단 한명 제외 (완주자가 1명 적음)
        if participant[i] != completion[i] :
            answer = participant[i]
            print(participant[i])
            break
    if answer == '':
        answer = participant[-1]
    return answer


participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

re = solution(participant, completion)
print(re)

print("====================")
