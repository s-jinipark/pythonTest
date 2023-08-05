
def solution(expense, participants):
    answer = 0

    left = 100
    right = expense
    while left <= right:
        mid = (left + right) // 2
        print(mid)
        mid = mid // 100 * participants
        if mid >= expense:
            answer = mid
            right = mid - 100
        else:
            left = mid + 100

    return answer


expense = 200000
participants = 12

re = solution(expense, participants)
print(re)