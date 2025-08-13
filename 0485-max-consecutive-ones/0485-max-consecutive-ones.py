class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m=""
        for i in nums:
                m+=(str(i))
        Max=[]     
        S=m.split("0")
        for i in S:
            Sum=0
            for j in i:
                Sum+=int(j) 
            Max.append(Sum) 
        return max(Max)