class Solution(object):
    def isPalindrome(s: str) -> bool:
    #preprocessing
        lower = s.lower()
        allowed = "abcdefghijklmnopqrstuvwxyz1234567890"
        for element in lower:
            if element not in allowed:
                lower = lower.replace(element, " ")
        check = lower.replace(" ", "")

        #edge
        if len(check)==0 or len(check)==1:
            return True

        #for even strings
        if(len(check)%2==0):
            pointer1= len(check)//2
            pointer2= (len(check)//2) -1

            while(check[pointer1] == check[pointer2]):
                if pointer1 != len(check)-1:
                    pointer1+=1
                    pointer2+=-1
                else:
                    return True
            return False
        #odd strings
        else:
            pointer1 = ((len(check)-1)//2)+1
            pointer2 = ((len(check)-1)//2)-1
            while(check[pointer1] == check[pointer2]):
                if pointer1 != len(check)-1:
                    pointer1+=1
                    pointer2+=-1
                else:
                    return True
            return False
