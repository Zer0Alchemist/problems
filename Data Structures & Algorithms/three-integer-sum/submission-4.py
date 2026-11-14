class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        lst = []
        i = 0
        nums.sort()

        while i < len(nums):
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    if tuple(sorted([nums[i], nums[left], nums[right]])) in seen:
                        right -= 1
                        left += 1
                        continue
                    seen.add(tuple(sorted([nums[i], nums[left], nums[right]])))
                    lst.append([nums[i], nums[left], nums[right]])

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    right -= 1
                    left += 1
                
            i += 1

        return lst