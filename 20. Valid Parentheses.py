class Solution:
    def isValid(self, s: str) -> bool:
        p = {
        "{": "}",
        "[": "]",
        "(": ")"
        }
        stack = deque()
        for letter in s:
            if letter in p:
                stack.append(letter)
            elif letter == "]" or letter == "}" or letter == ")":
                if stack and letter == p[stack[len(stack)-1]]:
                        stack.pop()
                else:
                    return False

        return not stack
            