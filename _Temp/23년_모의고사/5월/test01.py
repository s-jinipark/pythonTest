
# 커튼_빈칸채우기

def solution(width, curtain):
    answer = 0
    curtain.sort()

    left, right = 0, len(curtain) - 1
    print(left, right)
    while left <= right:
        mid = (left + right) // 2
        if curtain[mid]  >=  width:   # <- 빈 칸 [ >= ]
            answer = curtain[mid]
            right = mid - 1   # <- 빈 칸 [ mid - 1 ]
        else:
            left = mid + 1   # <- 빈 칸 [ mid + 1 ]

    return answer


'''

'''

width = 200
curtain = [100, 300, 250, 190]

an = solution(width, curtain)
print(an)