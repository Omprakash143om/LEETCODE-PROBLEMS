class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l1=[]
        for i in range(left,right+1):
            a=str(i)
            b=True
            for j in range(len(a)):
                if int(a[j])==0 or i%int(a[j])!=0:
                    b=False
                    break
            if b:
                l1.append(i)
        return l1