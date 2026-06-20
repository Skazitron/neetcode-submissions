class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        equivalences = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for x in s:
            if x in equivalences:
                if len(stack) <= 0:
                    return False
                elif stack[-1] != equivalences[x]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(x)

        return len(stack) == 0