# Last updated: 7/14/2026, 11:57:45 AM
class Solution:
    def reverseVowels(self, s: str) -> str:
        l=0
        r=len(s)-1
        st=list(s)
        li=["A","E","I","O","U","a","e","i","o","u"]
        while(l<r):
            if st[l] in li and st[r] in li:
                st[l],st[r]=st[r],st[l]
                l+=1
                r-=1
            elif st[l] in li and st[r] not in li:
                r-=1
            else :
                l+=1
        s="".join(st)
        return s


        