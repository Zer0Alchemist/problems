class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lst = []
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            val = numbers[left] + numbers[right]
            
            if val == target:
                lst.append(left + 1)
                lst.append(right + 1)
                break
            elif val > target:
                right -= 1
            elif val < target:
                left += 1
        
        return lst