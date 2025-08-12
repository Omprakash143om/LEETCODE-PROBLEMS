class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict1={}
        for i,val in enumerate(nums):
            if val in dict1 and abs(i-dict1[val])<=k:
                return True
            else:
                dict1[val]=i
        return False