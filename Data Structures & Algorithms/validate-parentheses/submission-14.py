class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stack = []
        matches = {')': '(', ']': '[', '}': '{'}

        for ss in s:
            if ss in '([{':
                stack.append(ss)
            elif ss in ')]}':
                if not stack or stack.pop() != matches[ss]:
                    return False

        return not stack  # <-- controllo finale: stack deve essere vuoto