
def solution1(tmplist) :
    # . 버블 정렬
    print(". 버블 정렬")
    for i in range(len(tmplist)):
        for j in range(len(tmplist)-1) :  # -1 이 꼭 있어야 함
            if tmplist[j] > tmplist[j+1] : # 큰 거 뒤로
                tmp = tmplist[j+1]
                tmplist[j + 1] = tmplist[j]
                tmplist[j] = tmp
        print(tmplist)


def solution2(tmplist) :
    # . 선택 정렬
    print(". 선택 정렬")
    # ***** 이부분 중요
    for i in range(len(tmplist)):
        minidx = i
        for j in range(i, len(tmplist)):
            if tmplist[j] < tmplist[minidx]:
                minidx = j
        if minidx != i :  # min 값이 바뀌었다면
            temp = tmplist[i]
            tmplist[i] = tmplist[minidx]
            tmplist[minidx] = temp
        print(tmplist)


def solution3(tmplist) :
    # . 삽입 정렬
    print(". 삽입 정렬")
    # ***** 이부분 중요
    for i in range(1, len(tmplist)) :  # idx 1부터 시작한다는 점
        backup = tmplist[i]  # 일단 백업
        idx = i-1  # 인덱스는 바로 앞으로 셋팅

        while idx >=0 and backup < tmplist[idx] :
            tmplist[idx+1] = tmplist[idx]
            idx -= 1  # 줄줄이 옮김

        tmplist[idx+1] = backup  # 여기선 idx 를 하나 늘려 줌 (헷갈림 . ㅠ)
        print(tmplist)


# def solution1(tmp) :
#     # . 버블 정렬
#     #  1. 앞에서부터 현재 원소와 바로 다음의 원소를 비교한다
#     #  2. 현재 원소가 다음 원소보다 크면 원소를 교환한다
#     #  3. 다음 원소로 이동하여 해당 원소와 그 다음 원소를 비교한다
#     for i in range(len(tmp)) :
#         for j in range(len(tmp)-1) :   # -1 안하면 오류남 => IndexError: list index out of range
#             if tmp[j] > tmp[j+1] :
#                 tval = tmp[j]
#                 tmp[j] = tmp[j+1]
#                 tmp[j + 1] = tval
#         print(tmp)
#
#
# def solution2(tmp) :
#     # . 선택 정렬
#     #  1. 주어진 리스트(배열)에서 최소값을 찾는다
#     #  2. 최솟값을 맨 앞 자리의 값과 교환한다
#     #  3. 맨 앞 자리를 제외한 나머지 값들 중 최소값을 찾아 위와 같은 방법(1,2번 과정)으로 반복한다
#     idx = 0
#     min_val = 999999
#     min(tmp)
#     tmp_val = 0
#     for i in range(len(tmp)) :
#         #print(tmp[i])
#         for j in range(i, len(tmp)) :
#             if min_val > tmp[j] :
#                 idx = j
#                 min_val = tmp[j]
#             #print(tmp[j])
#         tmp_val = tmp[idx]
#         tmp[idx] = tmp[i]
#         tmp[i] = tmp_val
#         idx = 0
#         min_val = 999999
#         #print()
#         print(tmp)
#
#
# def solution3(tmplist) :
#     # . 삽입 정렬
#     #  1. 현재 타겟이 되는 숫자와 이전 위치에 있는 원소들을 비교한다
#     #     (첫 번째 타겟은 두번째 원소부터 시작한다)
#     #  2. 타겟이 되는 숫자가 이전 위치에 있던 원소보다 작다면 위치를 서로 교환한다
#     #  3. 그 다음 타겟을 기준으로 다시 1,2 과정을 반복한다
#     for i in range(1, len(tmplist)):    # 1부터 시작
#         standard = tmplist[i]  # standard 에 backup
#         idx = i - 1  # 0, ...
#
#         while idx >= 0 and standard < tmplist[idx]:
#             tmplist[idx+1] = tmplist[idx]  # 0 의 값을 1 에 넣는다(뒤로 이동)
#             idx -= 1    # -1 하면서 계속한다
#
#         tmplist[idx + 1] = standard
#         print(tmplist)
# # ** 삽입정렬은 ... 일단 ...


def main() :
    print('정렬')
    tmplist = [10, 2, 6, 4, 3, 7, 5]
    print(tmplist)
    print()
    solution1(tmplist)   # 버블 정렬
    print()
    tmplist = [10, 2, 6, 4, 3, 7, 5]
    solution2(tmplist)   # 선택 정렬
    print()
    tmplist = [10, 2, 6, 4, 3, 7, 5]
    solution3(tmplist)   # 삽입 정렬
    print()

if __name__ == '__main__' :
    main()