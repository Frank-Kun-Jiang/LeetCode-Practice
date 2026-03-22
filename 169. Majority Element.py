def majorityElement(nums: List[int]) -> int:
    if len(nums)==1:
        return nums[0]
    end={}
    for i in range(len(nums)):
        if end.get(nums[i],0)==0:
            end[nums[i]]=1
        else:
            end[nums[i]]+=1
            if end[nums[i]]>=len(nums)/2:
                return nums[i]

print(majorityElement([2]))