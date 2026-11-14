class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lst = [0] * len(temperatures)
        stack = []

        for n in range(len(temperatures)):
            while stack and temperatures[n] > temperatures[stack[-1]]:
                last = stack.pop()
                lst[last] = n - last

            stack.append(n)

        return lst