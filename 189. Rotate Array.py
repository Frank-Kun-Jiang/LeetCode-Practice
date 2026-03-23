def rotate(nums: List[int], k: int) -> None:
    result=[]
    k=k%len(nums)
    for i in range(len(nums)-k,len(nums)):
        result.append(nums[i])
    for i in range(len(nums)-k):
        result.append(nums[i])
    nums[:]=result[:]


num=[-1]
rotate(num,2)
print(num)

'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

三次反转

这是这题的经典最优解。

核心思想：

例如：
[1,2,3,4,5,6,7], k=3

目标：
[5,6,7,1,2,3,4]

步骤：

整体反转
[7,6,5,4,3,2,1]
反转前 k 个
[5,6,7,4,3,2,1]
反转后 n-k 个
[5,6,7,1,2,3,4]

'''