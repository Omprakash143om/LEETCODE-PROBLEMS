class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A")>=2:
            return False
        elif s.count("LLL")>=1:
            return False
        else:
            return True