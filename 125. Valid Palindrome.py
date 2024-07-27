class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "" or s == " ":
            return True
        s = s.lower()
        right = len(s) -1
        left = 0
        while left < right:
            if not s[left].isalnum():
                left +=1
            if not s[right].isalnum():
                right -= 1
            if s[left].isalnum() and s[right].isalnum():
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
        return True
