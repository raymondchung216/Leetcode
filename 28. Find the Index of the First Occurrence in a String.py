class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = -1
        found = -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                for j in range(len(needle)):
                    if (i < len(haystack) and haystack[i] == needle[j]):
                        if j == (len(needle)-1):
                            found = (i - (j))
                    else:
                        i+=1
                        break
                    i+=1
                if found != -1:
                    return found
        return found