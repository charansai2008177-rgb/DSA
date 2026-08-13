class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(ch for ch in s if ch.isalnum())
        cleaned = cleaned.lower()
        if cleaned == cleaned[::-1]:
            return True
        return False