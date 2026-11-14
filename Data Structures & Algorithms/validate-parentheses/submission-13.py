class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) == 1:
            return False

        brackets = []

        for n in s:
            if n.isalpha():
                continue
            if n == "[" or n == "{" or n == "(":
                brackets.append(n)
                continue
            else:
                if not brackets:
                    return False

            last = brackets[-1]

            if n == "]" and last != "[":
                return False
            if n == "}" and last != "{":
                return False
            if n == ")" and last != "(":
                return False

            brackets.pop()

        return len(brackets) == 0