# Last updated: 7/14/2026, 11:57:42 AM
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = math.sqrt(num)
        if n == int(n):
            return True
        else :
            return False
        return True