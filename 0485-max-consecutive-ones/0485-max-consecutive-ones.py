class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a=nums.count(0)
        currentcount=0
        while a!=0:
            b=nums.index(0)
            if currentcount<b:
                currentcount=b
            if b!=len(nums)-1:
                nums=nums[b+1:]
            a-=1
        if 0 not in nums:
            if currentcount<len(nums):
                currentcount=len(nums)
        return currentcount