import heapq


def solution(patients, k):
    answer = 0
    pq = []
    '''
    patients의 원소는 [1, 응급도, 환자 번호] 또는 [0] 형태입니다.
    각 patients 원소의 첫 번째 원소가 1이면 접수, 0이면 진료하는 것을 의미합니다.
    '''
    for i in range(len(patients)):
        if patients[i][0] == 1:  # if patients[i][0] == 0:
            heapq.heappush(pq, [-patients[i][1], patients[i][2]])
        else:
            answer += 1
            if pq[0][1] == k:
                break
            heapq.heappop(pq)

    return answer


patients = [[1, 10, 1], [1, 20, 2], [0], [0], [1, 30, 3], [0]]
k = 1

re = solution(patients, k)
print(re)