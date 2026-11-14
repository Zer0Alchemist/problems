class Solution:
        def isValid(self, s: str) -> bool:
            s1 = list(s)
            stack = []
            if len(s) == 1:
                return False
            for char in s1:
                if char == "[" or char == "{" or char == "(":
                    stack.append(char)
                    continue
                else:
                    if not stack:
                        return False

                top = stack[-1]

                if char == "]" and top != "[":
                    return False
                elif char == "}" and top != "{":
                    return False
                elif char == ")" and top != "(":
                    return False

                stack.pop()

            return not stack