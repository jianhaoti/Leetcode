class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        operators = "+-*/"
        for element in tokens:
            if element not in operators:
                numStack.append(int(element))
            else:
                a = numStack.pop()
                b = numStack.pop()

                if element == "+":
                    numStack.append(b+a)
                elif element == "-":
                    numStack.append(b-a)
                elif element == "*":
                    numStack.append(b*a)
                elif element == "/":
                    if b/a > 0:
                        numStack.append(b//a)
                    elif b/a < 0:
                        numStack.append(b//a +1)
                    else:
                        numStack.append(0)

        return numStack[0]