class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)
        set1=set(candyType)
        allowedcandies=int(n/2)
        if len(set1)<=allowedcandies:
            return len(set1)
        else:
            return allowedcandies     