class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lst = []

        for n in tokens:
            if n != "+" and n != "-" and n != "*" and n != "/":
                lst.append(int(n))
            else:
                if lst and n == "+" and len(lst) >= 2:
                    b = lst.pop()
                    a = lst.pop()
                    val = a + b
                    lst.append(val)
                elif lst and n == "-" and len(lst) >= 2:
                    b = lst.pop()
                    a = lst.pop()
                    val = a - b
                    lst.append(val)
                elif lst and n == "/" and len(lst) >= 2:
                    b = lst.pop()
                    a = lst.pop()
                    val = int(a / b)
                    lst.append(val)
                elif lst and n == "*" and len(lst) >= 2:
                    b = lst.pop()
                    a = lst.pop()
                    val = a * b
                    lst.append(val)

        return lst[0]