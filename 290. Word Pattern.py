class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split()
        if len(arr) != len(pattern):
            print(len(arr), len(s) )
            return False
        tupleSet= set()
        wordSet = set()
        letterSet = set()
        for letter,word in zip(pattern,arr) :
            print(letter, word)
            if letter not in letterSet and word not in wordSet:
                letterSet.add(letter)
                wordSet.add(word)
                tupleSet.add((letter,word))
            else:
                if (letter,word) not in tupleSet:
                    return False
        return True
        