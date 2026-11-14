class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "".join(n for n in s if n.isalnum())
        s1 = s1.upper()
        l = len(s1) - 1

        i = 0
        while i < l:
            if s1[i] != s1[l]:
                return False
            i += 1
            l -= 1
        return True