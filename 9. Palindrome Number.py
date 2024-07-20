class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        if x < 0 :
            return False
        reverse = 0
        while num > 0:
            reverse = (reverse * 10) + (num % 10)
            num //= 10
        print(reverse)
        return x == reverse


# Converted integer to string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        strX = str(x)
        left = 0
        right = len(strX) - 1
        while left < right and left != right:
            if strX[left] == strX[right]:
                left += 1
                right -= 1
            else:
                return False
        return True