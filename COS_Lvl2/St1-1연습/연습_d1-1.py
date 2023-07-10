
def solution1(inp) :
    answer = 0
    tmp = [0] * 6  # 사이즈 순서대로.. fix
    for i in inp:
        if i =='XS':
            tmp[0] += 1
        elif i == 'S':
            tmp[1] += 1
        elif i == 'M':
            tmp[2] += 1
        elif i == 'L':
            tmp[3] += 1
        elif i == 'XL':
            tmp[4] += 1
        elif i == 'XXL':
            tmp[5] += 1
    print(tmp)
    return answer


shirtSize = ["XS", "S", "L", "L", "XL", "S"]

re = solution1(shirtSize)

'''
return 하는 리스트에는 [ "XS" 개수, "S" 개수, "M" 개수, "L" 개수, "XL" 개수, "XXL" 개수] 순서로
들어있어야 합니다.

=> [1, 2, 0, 2, 1, 0]
'''