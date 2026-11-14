class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_check = []
        for n in nums:
            if n not in dup_check:
                dup_check.append(n)
                continue
            
            if n in dup_check:
                return True

        return False