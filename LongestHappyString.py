class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        if a+b+c == 1:
            if a == 1:
                return "a"
            if b == 1:
                return "b"
            if c == 1:
                return "c"

        else:
            arr = [a,b,c]
            s = ""
            while (a!=0 and b!=0) or (a!=0 or c!=0) or (b!=0 and c!=0):
                arr = sort(arr)
                arr[-1] = arr[-1] - 2

            if a!=0:
                nonZero = 'a'

            elif b!=0:
                nonZero = 'b'

            elif c!= 0:
                nonZero = 'c'

            if s[-1] == nonZero and s[-2] == nonZero:
                return s
            elif s[-1] == nonZero and s[-2] != nonZero:
                return s+ nonZero
            else:
                return s + nonZero + nonZero

            return s
