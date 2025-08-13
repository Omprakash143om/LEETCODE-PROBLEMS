class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m=""
        for i in nums:
                m+=(str(i))
        Max=[]     
        S=m.split("0")
        for i in S:
            Max.append(len(i))
        return max(Max)