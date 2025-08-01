class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        a=int(max(nums))
        c=nums.index(a)
        nums.remove(a)
        squarenum=list(map(lambda x:x*2,nums))
        b=False
        for i in squarenum:
            if a>=i:
                b=True
            else:
                b=False
                break
        if b==True:
            return c
        else:
            return -1