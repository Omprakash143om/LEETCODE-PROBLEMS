class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        a=int(max(nums))
        c=nums.index(a)
        nums.remove(a)
        squarenum=list(map(lambda x:x*2,nums))
        b=True
        for i in squarenum:
            if a<i:
                b=False
                break
        if b:
            return c
        else:
            return -1