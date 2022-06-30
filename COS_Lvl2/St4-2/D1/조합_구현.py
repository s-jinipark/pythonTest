# 1. 조합(Combination) - visit 리스트로 사용 여부 체크하는 방법
def combi1(nums, n, r, start):
    global visit1
    if r == 0:
        for i in range(len(nums)):
            if visit1[i]:
                print(nums[i], " ", end="")
        print()
        return

    for i in range(start, len(nums)): # 영상 코드 중 start가 빠져 있어서 1개 원소들이 출력되었습니다. start로 수정합니다.
        visit1[i] = True
        combi1(nums, n, r-1 , i+1)
        visit1[i] = False



# 2. 조합(Combination) - 재귀 호출로 사용 여부 결정하는 방법   nCr
def combi2(nums, ans, n, r, idx, target):
    if r == 0:
        for i in ans:
            print(i, " ", end='')

        print()
        return

    if target == n:
        return

    ans[idx] = nums[target]
    combi2(nums, ans, n, r-1, idx+1, target+1)   # 선택
    combi2(nums, ans, n, r, idx, target + 1)     # 선택 안함


# 3. 중복 조합
def recombination(nums, ans, n, r, idx, target):
    if r == 0:
        for i in ans:
            print(i, " ", end='')
        print()
        return

    if target == n:
        return

    ans[idx] = nums[target]
    recombination(nums, ans, n, r - 1, idx+1, target)
    recombination(nums, ans, n, r, idx, target+1)


# 1. 조합(Combination) - visit 리스트로 사용 여부 체크하는 방법
nums = [1,2,3,4]
visit1 = [False for _ in range(len(nums))]
print("1. 조합(Combination) - visit 리스트로 사용 여부 체크하는 방법")
combi1(nums, 4, 2, 0)
print()

# 2. 조합(Combination) - 재귀 호출로 사용 여부 결정하는 방법   nCr
r = 3
ans = [0 for _ in range(r)]
print("# 2. 조합(Combination) - 재귀 호출로 사용 여부 결정하는 방법   nCr")
combi2(nums, ans, 4, r, 0, 0)
print()

# 3. 중복 조합
r = 2
ans2 = [0 for _ in range(r)]
print("# 3. 중복 조합")
recombination(nums,ans2, 4, r, 0, 0)


