def solution(n, arr1, arr2):
    answer = []

    # 이진수를 만들어야 함
    '''
    [참조] https://security-nanglam.tistory.com/508
    
    n진수  → 10진수
    python에서는 기본적으로 int() 라는 함수를 지원합니다.
        print(int('111',2))
        print(int('FFF',16))
    
    10진수  → 2, 8, 16진수
    2, 8, 16진수는 bin(), oct(), hex() 함수를 지원합니다.
        print(bin(10))   ->  0b1010
        print(oct(10))   ->  0o12
        print(hex(10))   ->  0xa
    
    --------------------    
    https://m.blog.naver.com/wideeyed/221528194867
    
    Python에서 문자열.zfill(길이) 함수를 통해 왼쪽에 0을 채울 수 있습니다.

    또한 문자열.rjust(길이, 채울문자), 문자열.ljust(길이, 채울문자) 함수를 통해 왼쪽, 오른쪽을 채울 수 있습니다.

    '''
    for i in range(n):
        #print(bin(arr1[i]).zfill(5))
        print(str(bin(arr1[i]))[2:].zfill(n))
        tmp1 = str(bin(arr1[i]))[2:].zfill(n)
        tmp2 = str(bin(arr2[i]))[2:].zfill(n)
        res = ""
        for j in range(n):
            if tmp1[j] == '0' and tmp2[j] == '0':
                res += ' '
            else :
                res += '#'
        answer.append(res)
    return answer


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

re = solution(n, arr1, arr2)
print(re)

print("====================")
