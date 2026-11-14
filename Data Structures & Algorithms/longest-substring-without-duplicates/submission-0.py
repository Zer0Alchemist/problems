class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        left = 0
        res = 0
        lst = list(s)

        for right in range(len(lst)):
            while lst[right] in sett:
                sett.remove(lst[left])
                left += 1

            sett.add(lst[right])
            if len(sett) > res:
                res = len(sett)

        return res