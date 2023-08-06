
def solution(phrase):
    answer = []
    for p in phrase:
        print(p.replace(' ', ''))
        tmp = p.replace(' ', '')
        answer.append(len(tmp)*100)
    return answer

phrase = ["Enjoy your life", "I LOVE YOU", "Just try"]

re = solution(phrase)
print(re)