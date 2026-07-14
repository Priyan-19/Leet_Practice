# Last updated: 7/14/2026, 11:58:30 AM
class Solution:
    def intToRoman(self, num: int) -> str:
        num_dict ={
            1:"I",4:"IV",
            5:"V",9:"IX",
            10:"X",40:"XL",
            50:"L",90:"XC",
            100:"C",500:"D",
            1000:"M",900:"CM",400:"CD"
        }
        nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        re =""
        for i in nums:
            while num>=i:
                re+=num_dict[i]
                num-=i
        return re