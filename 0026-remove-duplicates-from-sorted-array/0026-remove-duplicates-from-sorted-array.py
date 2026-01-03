class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=set(nums)
        while len(nums)>len(l):
            list1=[]
            for i in nums:
                if i in list1:
                    nums.remove(i)
                else:
                    list1.append(i)
        return len(nums)