class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = nums1.copy()
        x,y=0,0
        for i in range(len(nums1)):
            if x==m:
                nums1[i]=nums2[y]
                y=y+1
            elif y==n:
                nums1[i]=nums3[x]
                x=x+1
            elif nums3[x]<nums2[y]:
                nums1[i]=nums3[x]
                x=x+1
            else:
                nums1[i]=nums2[y]
                y=y+1