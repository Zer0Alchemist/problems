class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst = []
        seen = set()
        i = 0
        nums.sort()

        while i < len(nums):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    if tuple(sorted([nums[i], nums[j], nums[k]])) in seen:
                        j += 1
                        k -= 1
                        continue
                    valid = sorted([nums[i], nums[j], nums[k]])
                    seen.add(tuple(valid))
                    lst.append(valid)

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
                    j += 1
                
            i += 1

        return lst