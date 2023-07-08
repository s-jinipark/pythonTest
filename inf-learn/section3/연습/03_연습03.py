
##### 카드 역배치(정올 기출)
def solution():
    answer = 0
    # 카드 배열을 만듬
    cards = [0] * 21
    for i in range(1, 20+1):
        cards[i] = i
    #print(cards)

    change = [0] * 21
    # 10개의 구간 순서대로 뒤집는 작업
    for i in inp:
        #print(i)
        s, e = i
        print(s, e)
        cnt = 0
        for j in range(s, e+1):
            change[j] = cards[e-cnt]
            cnt += 1
        #print(cards)
        #print(change)
        # copy 하는 작업
        for k in range(s, e+1):
            cards[k] = change[k]
        print(cards)
        # idx 1 부터 출력 필요
    return answer

'''
1부터 20까지 오름차순으로 놓인 카드들에 대해, 입력으로 주어진 10개의 구간 순서대로 
뒤집는 작업을 했을 때 마지막 카드들의 배치를 한 줄에 출력한다.
'''
inp = [
    [5, 10],
    [9, 13],
    [1, 2],
    [3, 4],
    [5, 6],
    [1, 2],
    [3, 4],
    [5, 6],
    [1, 20],
    [1, 20]
]
re = solution()
print(re)
#=>
