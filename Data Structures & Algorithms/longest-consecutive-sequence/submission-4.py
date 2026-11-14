class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        seen = set()

        for n in nums:
            if n in seen:
                continue
            seen.add(n)

        lst = sorted(list(seen))

        res = 0
        count = 1
        for i in range(len(lst) - 1):
            if lst[i] + 1 != lst[i + 1] and count > res:
                res = count
                count = 1
                continue
            if lst[i] + 1 != lst[i + 1] and count <= res:
                count = 1
                continue
            
            count += 1

        if count > res:
            res = count
        
        return res