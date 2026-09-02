# Last updated: 9/2/2026, 11:12:04 AM
1class Solution:
2    def divide(self, dividend: int, divisor: int) -> int:
3
4        # Handle overflow case
5        if dividend == -2147483648 and divisor == -1:
6            return 2147483647
7
8        # Determine the sign
9        negative = (dividend < 0) != (divisor < 0)
10
11        # Work with positive numbers
12        dividend = abs(dividend)
13        divisor = abs(divisor)
14
15        result = 0
16
17        # Subtract divisor using powers of 2
18        while dividend >= divisor:
19
20            temp = divisor
21            multiple = 1
22
23            while dividend >= (temp << 1):
24                temp <<= 1
25                multiple <<= 1
26
27            dividend -= temp
28            result += multiple
29
30        if negative:
31            result = -result
32
33        return result