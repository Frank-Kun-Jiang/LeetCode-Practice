def removeDuplicates(nums: List[int]) -> int:
    result=[]
    k=0
    if len(nums)==0:
        return 0
    result.append(nums[0])
    for i in range(len(nums)):
        if nums[i]>result[k]:
            k+=1
            result.append(nums[i])
    for i in range(len(result)):
            nums[i] = result[i]
    return k+1


print(removeDuplicates([1,1,2]))