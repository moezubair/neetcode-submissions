class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Input: two strings
        # Output: Boolean
        # "aec" - > "abcde" . a

        s_i = 0
        for c in t:
            if s_i < len(s) and c == s[s_i]:
                s_i += 1
        
        return s_i == len(s)
            