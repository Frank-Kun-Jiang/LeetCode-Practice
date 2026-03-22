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


def BestMajorityElement(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

#使用两两抵消，投票算法