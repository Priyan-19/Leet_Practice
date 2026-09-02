# Last updated: 9/2/2026, 12:29:05 PM
1from typing import List
2from bisect import bisect_right
3
4class TopVotedCandidate:
5
6    def __init__(self, persons: List[int], times: List[int]):
7        self.times = times
8        self.winners = []
9
10        votes = {}
11        leader = -1
12
13        for person in persons:
14            votes[person] = votes.get(person, 0) + 1
15
16            if votes[person] >= votes.get(leader, 0):
17                leader = person
18
19            self.winners.append(leader)
20
21    def q(self, t: int) -> int:
22        i = bisect_right(self.times, t) - 1
23        return self.winners[i]