class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[]
        for i in operations:
            Sum=0
            if i.isdigit():
                record.append(int(i))
            elif i=="+":
                Sum=record[-1]+record[-2]
                record.append(Sum)
            elif i=="D":
                a=record[-1]*2
                record.append(a)
            elif i=="C":
                record.pop()
            else:
                record.append(int(i))
        return sum(record)      