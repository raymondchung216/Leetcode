# O(mn) where m is the longest word
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        longest = strs[0]
        for word in strs:
            if not word or longest[0] != word[0]:
                return ""
            i = 0
            while i < len(word) and i < len(longest) and longest[i] == word[i]:
                i += 1
            longest = longest[:i]
        return longest

# O(nlogn) need to sort
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        firstWord = strs[0]
        lastWord = strs[len(strs)-1]
        i = 0
        while i < len(firstWord) and i < len(lastWord) and firstWord[i] == lastWord[i]:
            i += 1
        return firstWord[:i]