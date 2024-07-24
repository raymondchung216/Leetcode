class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for letter in t:
            if (i < len(s) and letter == s[i]):
                i += 1
        return (i == len(s))
        
    # Other solution would be to find the powerset of s and insert into hashmap

        