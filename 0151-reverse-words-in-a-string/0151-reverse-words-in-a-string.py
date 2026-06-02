class Solution:
    def reverseWords(self, s: str) -> str:
        rever = s[::-1]
        re= " ".join(word[::-1] for word in rever.split())
        return re
        