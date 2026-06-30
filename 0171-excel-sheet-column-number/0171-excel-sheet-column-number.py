class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        re=0
        for i in columnTitle:
            t = ord(i)-(ord("A")-1)
            re = re*26+t
        return re
