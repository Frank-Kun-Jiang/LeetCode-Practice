def removeDuplicates(nums: List[int]) -> int:
    if len(nums)==0:
        return 0
    total=1
    repeated=0
    for rightpoint in range(1,len(nums)):
        if nums[rightpoint]!=nums[rightpoint-1]:
            repeated=0
            nums[total]=nums[rightpoint]
            total+=1
        elif repeated==0:
            nums[total]=nums[rightpoint]
            total+=1
            repeated+=1
    return total

print(removeDuplicates([0,0,1,1,1,1,2,3,3]))