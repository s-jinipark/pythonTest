
def solution(nums):
    #answer = -1
    answer = 0
    # 3 개 이상이므로 3 중으로
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                #print(str(nums[i]) + "/" + str(nums[j]) + "/" + str(nums[k])  )
                tmp = nums[i] +  nums[j] + nums[k]
                #print(tmp)
                #print(is_prime(tmp))
                if is_prime(tmp) :
                    answer+=1
    return answer


def is_prime(num):
    rtn = True
    for i in range(2,num):
        #print(i)
        if num%i == 0 : 
            rtn = False
            break
    return rtn

#n = [1,2,3,4]	
n = [1,2,7,6,4]	
an = solution(n)
print("=====")
print(an)