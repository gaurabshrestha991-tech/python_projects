class Solution:
    def lengthofLastWord(self, s: str) -> int:
        length = 0
        
        for i in range(len(s) - 1, -1, -1):
                if s[i] == ' ':
                    if length > 0:
                        break
                else:
                    length += 1
        return length
                    