import setuptools.command.easy_install

def solution(n, words):
    answer = [0,0]

    # 중복 검사 하기 위해
    setw = set()
    setw.add(words[0])

    for i in range(1, len(words)) :
        #print(words[i-1] , words[i])
        if words[i-1][-1] ==  words[i][0] and words[i] not in setw :
            setw.add(words[i])
        else :
            # 몇번째 사람인지
            # (그 사람의) 몇변째 대답인지
            # ***** 이부분 중요
            answer[0] = i % n + 1  # +1 해주어야 함
            answer[1] = i // n + 1
            break
        #print(answer)
    return answer

n = 3
words = ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']
res = solution(n, words)
print(res)     # [3, 3]

n = 5
words = ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive']
res = solution(n, words)
print(res)     # [0, 0]

n = 2
words = ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']
res = solution(n, words)
print(res)    # [1, 3]

