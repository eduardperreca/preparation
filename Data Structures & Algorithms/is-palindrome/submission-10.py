class Solution:
    def isPalindrome(self, s: str) -> bool:
        otherStr = ''
        for c in s:
            if c.isalnum():
                otherStr += c.lower()
        return otherStr == otherStr[::-1]