class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow=-1
        for fast in range(0,len(nums)):
            if nums[fast]!=0:
                slow+=1
                nums[slow],nums[fast]=nums[fast],nums[slow]
        return nums