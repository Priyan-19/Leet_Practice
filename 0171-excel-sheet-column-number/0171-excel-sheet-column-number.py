class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        re=0
        for i in columnTitle:
            te=ord(i)-64
            re=re*26+te
        return re
        