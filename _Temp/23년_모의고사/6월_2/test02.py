def func_a(sequence):
    size = len(sequence)
    cumulative_sum = [0] * (size + 1)

    for i in range(1, size + 1):
        cumulative_sum[i] = cumulative_sum[i - 1] + sequence[i - 1]

    return cumulative_sum

def func_b(cumulative_sum, section):
    start = section[0]
    end = section[1]

    return cumulative_sum[end+1] - cumulative_sum[start]

def solution(sequence, sections):
    cumulative_sum = func_a(sequence)  #@@@@@
    total_sum = 0
    print(cumulative_sum)

    for section in sections:
        total_sum += func_b(cumulative_sum, section) # @@@@@

    return total_sum



sequence = [3,1,5,4,2,1]
sections = [[0,2],[3,5],[2,4]]

an = solution(sequence, sections)
print(an)