def merge(sequence, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= right:
        if sequence[i] <= sequence[j]:
            temp[k] = @@@@@
            i += 1
        else:
            temp[k] = @@@@@
            j += 1
        k += 1

    while i <= mid:
        temp[k] = @@@@@
        i += 1
        k += 1
    while j <= right:
        temp[k] = @@@@@
        j += 1
        k += 1

    for idx in range(left, right + 1):
        sequence[idx] = @@@@@

def merge_sort(sequence, temp, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(sequence, temp, left, mid)
        merge_sort(sequence, temp, mid + 1, right)

        merge(sequence, temp, left, mid, right)

def solution(sequence):
    size = len(sequence)
    temp = [0] * size

    merge_sort(sequence, temp, 0, size - 1)

    return sequence

'''

'''
sequence = [6,2,-3, 0]

an = solution(sequence)
print(an)