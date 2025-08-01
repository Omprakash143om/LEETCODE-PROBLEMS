class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        targetnum=ord(target)
        s=[]
        for i in letters:
            a=ord(i)
            s.append(a)
        for i in range(len(s)):
            if targetnum<s[i]:
                return letters[i]
        else:
            return letters[0]