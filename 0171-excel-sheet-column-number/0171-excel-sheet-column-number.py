class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            # Convert letter to number (A=1, B=2, ..., Z=26)
            value = ord(char) - ord('A') + 1
            # Shift previous result by 26 (like base-26 number system)
            result = result * 26 + value
        return result