def canJump(nums: List[int]) -> bool:
    lastIndex=len(nums)-1
    i=0
    while i < len(nums):
        if lastIndex<=i+nums[i]:
            return True
        if nums[i]>=1:
            for x in range(1,nums[i]+1):
                if nums[i+x]+x>nums[i]:
                    i=i+x-1
                    break
                if x == nums[i] and nums[i+x]+x<=nums[x]:
                    return False
        else:
            return False
        i+=1
    
print(canJump([2,5,0,0]))

'''贪心算法 greedy algorithm
class Solution:
    def canJump(self, nums):
        farthest = 0
        for i, step in enumerate(nums):
            if i > farthest:
                return False
            farthest = max(farthest, i + step)
        return True
'''