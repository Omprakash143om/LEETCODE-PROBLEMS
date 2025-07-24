class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        l=[]
        res=[]
        for i in mat:
            for j in i:
                l.append(j)
        if r*c != len(l):
            return mat
        else:
            for index in range(r):
                res.append(l[index*c:index*c+c])
        return res

        