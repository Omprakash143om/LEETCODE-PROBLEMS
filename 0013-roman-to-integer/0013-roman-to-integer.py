class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        i=0
        while i < len(s):
            if i < len(s) - 1:
                if s[i] == "I" and s[i+1] == "V":
                    sum += 4
                    i += 1  # Skip next character
                elif s[i] == "I" and s[i+1] == "X":
                    sum += 9
                    i += 1
                elif s[i] == "X" and s[i+1] == "L":
                    sum += 40
                    i += 1
                elif s[i] == "X" and s[i+1] == "C":
                    sum += 90
                    i += 1
                elif s[i] == "C" and s[i+1] == "D":
                    sum += 400
                    i += 1
                elif s[i] == "C" and s[i+1] == "M":
                    sum += 900
                    i += 1
                else:
                    # Normal addition if no subtractive pair is found
                    if s[i] == "I":
                        sum += 1
                    elif s[i] == "V":
                        sum += 5
                    elif s[i] == "X":
                        sum += 10
                    elif s[i] == "L":
                        sum += 50
                    elif s[i] == "C":
                        sum += 100
                    elif s[i] == "D":
                        sum += 500
                    elif s[i] == "M":
                        sum += 1000
            else:
                # If it's the last character, just add its value
                if s[i] == "I":
                    sum += 1
                elif s[i] == "V":
                    sum += 5
                elif s[i] == "X":
                    sum += 10
                elif s[i] == "L":
                    sum += 50
                elif s[i] == "C":
                    sum += 100
                elif s[i] == "D":
                    sum += 500
                elif s[i] == "M":
                    sum += 1000

            i += 1  # Move to the next character
        
        return sum