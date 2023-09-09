
def solution(sequence, sorting):
    n = len(sequence)

    if sorting == "Insertion Sort":
        for i in range(1, n):
            key = sequence[i]
            j = i - 1
            while j >= 0 and sequence[j] > key:
                sequence[j + 1] = sequence[j]   #@@ @ @ @
                j -= 1
            sequence[j + 1] = key
    elif sorting == "Selection Sort":
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if sequence[j] < sequence[min_idx]:
                    min_idx = j
            temp = sequence[i]
            sequence[i] = sequence[min_idx]
            sequence[min_idx] = temp
    elif sorting == "Bubble Sort":
        for i in range(n):
            for j in range(0, n - i - 1):
                if sequence[j] > sequence[j + 1]:
                    temp = sequence[j ]
                    sequence[j ] = sequence[j + 1]
                    sequence[j + 1] = temp

    return sequence


'''

'''
sequence = [5,2,3,1]
sorting = "Selection Sort"
an = solution(sequence, sorting)
print(an)
