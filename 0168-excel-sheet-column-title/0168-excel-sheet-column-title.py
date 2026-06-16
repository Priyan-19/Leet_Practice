class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n=columnNumber
        re=""
        while(n>0):
            n-=1
            re=(chr(n%26+ord("A")))+re
            n//=26
        return(re)
