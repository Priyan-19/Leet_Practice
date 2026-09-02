# Last updated: 9/2/2026, 1:32:38 PM
1from collections import Counter
2
3class Solution:
4    def getHint(self, secret: str, guess: str) -> str:
5        bulls = 0
6        secret_count = Counter()
7        guess_count = Counter()
8
9        for i in range(len(secret)):
10            if secret[i] == guess[i]:
11                bulls += 1
12            else:
13                secret_count[secret[i]] += 1
14                guess_count[guess[i]] += 1
15
16        cows = 0
17
18        for digit in secret_count:
19            cows += min(secret_count[digit], guess_count[digit])
20
21        return f"{bulls}A{cows}B"