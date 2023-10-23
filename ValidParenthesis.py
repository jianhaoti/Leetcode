class Solution(object):
    def isValid(s: str) -> bool:
        tempParenthesis = []
        for char in s:
            if (char in "([{"):
                tempParenthesis.append(char)
            else:
                if not tempParenthesis:
                    return False
                elif (char == '}' and tempParenthesis[-1] == '{'):
                    tempParenthesis.pop()
                elif (char == ']' and tempParenthesis[-1] == '['):
                    tempParenthesis.pop()
                elif (char == ')' and tempParenthesis[-1] == '('):
                    tempParenthesis.pop()
                else:
                    return False
        if not tempParenthesis:
            return True
        else:
            return False

