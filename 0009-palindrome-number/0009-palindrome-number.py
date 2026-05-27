class Solution:
    def isPalindrome(self, x: int) -> bool:
        re = x 
        sum =0
        while x>0:
            ld = x%10
            sum = (10*sum)+ld
            x//=10
        if sum == re:
            return True
        else :
            return False

    