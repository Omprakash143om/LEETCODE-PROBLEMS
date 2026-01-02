class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        c1=0
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
            else:
                nums[c1]=nums[i]
                c1+=1
                print(c1)
        print(count)
        for i in range(-1,-(count+1),-1):
            nums[i]=0
            print(i)
        print(nums)