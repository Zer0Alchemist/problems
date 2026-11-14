class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = []

        for n in range(len(nums) - 1):
            for j in range(n + 1, len(nums)):
                if nums[n] + nums[j] == target:
                    lst.append(n)
                    lst.append(j)
                    return lst