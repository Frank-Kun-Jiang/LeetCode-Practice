def minSubArrayLen(target: int, nums: List[int]) -> int:
    left=0
    sum =0
    result=float("inf")
    for right in range(len(nums)):
        sum+=nums[right]
        while sum>=target:
            result= min(result,right-left+1)
            sum-=nums[left]
            left+=1
    if result==float("inf"):
        return 0
    else:
        return int(result)


print(minSubArrayLen(7,[2,3,1,2,4,3]))