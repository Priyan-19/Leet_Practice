class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''.join(map(str,digits))
        n=str(int(s)+1)
        li=[0]*len(n)
        for i in range(len(n)):
            li[i]=int(n[i])
        return(li)
        