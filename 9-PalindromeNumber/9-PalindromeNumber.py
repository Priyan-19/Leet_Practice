# Last updated: 7/14/2026, 11:58:31 AM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        re = str(x)
        if re == re[::-1]:
            return True
        else :
            return False

    