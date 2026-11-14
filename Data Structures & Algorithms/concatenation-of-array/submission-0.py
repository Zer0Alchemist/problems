class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        j = 0
        for n in nums:
            ans.append(n)
        for i in nums:
            ans.append(i)

        return ans