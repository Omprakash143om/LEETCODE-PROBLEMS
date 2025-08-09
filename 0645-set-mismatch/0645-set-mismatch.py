class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        duplicate = 0
        missing = 0
        # Step 1: Find duplicate
        for num in nums:
            if nums.count(num) == 2:
                duplicate = num
                break
        # Step 2: Find missing
        for i in range(1, n + 1):
            if i not in nums:
                missing = i
                break
        return [duplicate, missing]