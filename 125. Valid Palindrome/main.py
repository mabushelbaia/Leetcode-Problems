class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = "".join(ch.lower() for ch in s if ch.isalnum())
        return s2 == s2[::-1]