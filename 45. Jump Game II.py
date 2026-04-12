def jump(nums: List[int]) -> int:
    if len(nums)==1: return 0
    lastIndex=len(nums)-1
    result=0
    i=0
    while i<len(nums):
        maxstep=0
        maxindex=0
        result+=1
        for x in range(1,nums[i]+1):
            if i + x == lastIndex:
                return result
            if nums[i+x]+x>nums[i]:
                if nums[i+x]+x>maxstep:
                    maxindex=i+x
                    maxstep=nums[i+x]+x
        i=maxindex

print(jump([2,3,1,1,4]))