
# 프로그래머스 스타일 로 ...
def solution(n, lost, reserve):
    answer = 0

    # 자기거 먼저 돌리고,
    # 0 번 아닌 1번 부터 시작한다고 봄
    # 소트 먼저
    lost.sort()
    reserve.sort()
    tmp = 0

    for i in range(len(lost)):
        # 자신의 번호가 있는지
        #print( reserve.index(3) )  # try ~ except 구문 사용해야 함
        # 있을 경우 -1 로 만들자
        for j in range(len(reserve)):
            if lost[i] == reserve[j] :
                tmp += 1
                reserve[j] = -1
                lost[i] = -1   # *** 여기도 빼 주어야
                break  # 구제 받았으면 continue 해도 되지 않나?

    # 한번 더 돌아야 하나?  프로그래머스 통과는 함
    for i in range(len(lost)):
        if lost[i] == -1 :
            continue
        for j in range(len(reserve)):
            # 앞뒤를 본다
            if lost[i]-1 == reserve[j] :
                tmp += 1
                reserve[j] = -1
                break
            elif lost[i] + 1 == reserve[j]:
                tmp += 1
                reserve[j] = -1
                break

    # 구제한 사람 연습
    answer = n - len(lost) + tmp
    return answer

n = 5   # 전체 학생의 수

lost = [2,4]
reserve = [1,3,5]

re = solution(n, lost, reserve)
print('re :', re)
#=>
print('==============================')

n = 5   # 전체 학생의 수

lost = [2,4]
reserve = [3]

re = solution(n, lost, reserve)
print('re :', re)
#=>
print('==============================')

n =3

lost = [3]
reserve = [1]

re = solution(n, lost, reserve)
print('re :', re)
#=>
print('==============================')

n =5

lost = [4,5]
reserve = [3,4]

re = solution(n, lost, reserve)
print('re :', re)
#=> 4
print('==============================')