# Last updated: 7/14/2026, 11:58:28 AM
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        re=[]
        nums.sort()
        n=len(nums)
        for i in range(n):
            if nums[i]>0:
                break
            if i>0  and nums[i]==nums[i-1]:
                continue
            l,r=i+1,n-1
            while(l<r):
                
                su = nums[i]+nums[l]+nums[r]

                if su>0:
                    r-=1
                elif su<0:
                    l+=1
                else:
                    re.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while (l<r) and nums[l]==nums[l-1]:
                        l+=1
                    while (l<r) and nums[r]==nums[r+1]:
                        r-=1
        return re