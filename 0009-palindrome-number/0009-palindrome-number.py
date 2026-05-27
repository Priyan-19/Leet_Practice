class Solution:
    def isPalindrome(self, x: int) -> bool:
        re = str(x)
        if re == re[::-1]:
            return True
        else :
            return False

    