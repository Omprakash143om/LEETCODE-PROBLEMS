class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        if len(nums)>=2:
            for i in range(0,len(nums)):
                pivot=i
                if sum(nums[:pivot])==sum(nums[pivot+1:]):
                    return i
            else:
                return -1