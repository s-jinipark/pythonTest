
# 어떤 자연수 N(1 ≤ N ≤ 10,000,000)
# 10을 나타내는 방법은 10, 1+2+3+4 이다

#=> 시작 인덱스, 종료 인덱스를 투 포인터로 지정한 후 문제에 접근


n = 10

count = 1   # 자기 자신 계산
start_index = 1
end_index = 1
sum = 1

while end_index != n :
    if sum == n :
        print(start_index, end_index)
        count += 1
        end_index += 1
        sum += end_index
    elif sum > n :
        sum -= start_index
        start_index += 1
    else :
        end_index += 1
        sum += end_index
print(count)