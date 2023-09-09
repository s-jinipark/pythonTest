def solution(n):
    count = 0
    i = 333

    while True:
        k = i
        print(k)
        while k != 0:

            if k % 1000 == i :  #@ @ @ @ @:
                count += 1
                break
            else:
                k = k // 10

        if count == n :  #@ @ @ @ @:
            return i

        i += 1

'''
n	    result
1	    333
3	    2333
'''
#n = 1
n = 3

an = solution(n)
print(an)