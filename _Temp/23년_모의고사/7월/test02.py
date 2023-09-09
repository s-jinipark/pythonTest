def func_a(sequence):
    for num in sequence:
        count[num] += 1


def func_b():
    global answer
    for i in range(1, 1001):
        if count[i] == maxCount:
            answer = answer +1  #@ @ @ @ @

            return


def func_c():
    global maxCount
    maxCount = 0
    for i in range(1, 1001):
        maxCount = max(maxCount, count) # @ @ @ @ @)

def solution(sequence):
    global count
    count = [0] * 1001

    func_c()  # @ @ @ @ @
    func_a(sequence)  # @ @ @ @ @
    func_b()  # @ @ @ @ @

    return answer
'''

'''
sequence = [1,1,3,2,4,4,4]

an = solution(sequence)
print(an)