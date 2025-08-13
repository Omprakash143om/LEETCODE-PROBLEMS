class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        b=0
        maxcount=0
        for i in range(0,len(nums)):
            if nums[i]==1:
                b+=1
                if b>maxcount:
                    maxcount=b
            else:
                b=0
        return maxcount