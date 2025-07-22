class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        # Take the shortest word in the list
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            for word in strs:
                if word[i] != shortest[i]:
                    return shortest[:i]
        return shortest
                