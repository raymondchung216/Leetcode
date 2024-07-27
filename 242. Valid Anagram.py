class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        wordDict = dict()
        for letter in s:
            if letter in wordDict:
                wordDict[letter] += 1
            else:
                wordDict[letter] = 1
        
        for letter in t:
            if letter in wordDict:
                wordDict[letter] -= 1
                if wordDict[letter] == 0:
                    wordDict.pop(letter)
            else:
                return False
        if not wordDict:
            return True