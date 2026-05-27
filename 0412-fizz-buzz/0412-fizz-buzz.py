class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        re=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                re.append("FizzBuzz")
            elif i%3 ==0:
                re.append("Fizz")
            elif i%5 ==0:
                re.append("Buzz")
            else :
                re.append(str(i))
        return re


        