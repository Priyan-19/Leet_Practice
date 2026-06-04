class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        w=0
        for i in range(num1,num2+1):
            s=str(i)
            n=len(s)
            if n<3:
                continue
            for j in range(1,n-1):
                if s[j]>s[j-1] and s[j]>s[j+1]:
                    w+=1
                elif s[j]<s[j-1] and s[j]<s[j+1]:
                    w+=1
        return w