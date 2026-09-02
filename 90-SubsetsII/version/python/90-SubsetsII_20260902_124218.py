# Last updated: 9/2/2026, 12:42:18 PM
1class Solution:
2    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
3
4        trie = {}
5
6        for word in words:
7            node = trie
8            for char in word:
9                node = node.setdefault(char, {})
10            node["#"] = word
11
12        result = []
13        rows = len(board)
14        cols = len(board[0])
15
16        def dfs(r, c, node):
17            char = board[r][c]
18
19            if char not in node:
20                return
21
22            node = node[char]
23
24            if "#" in node:
25                result.append(node["#"])
26                del node["#"]
27
28            board[r][c] = "#"
29
30            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
31                nr, nc = r + dr, c + dc
32
33                if 0 <= nr < rows and 0 <= nc < cols:
34                    if board[nr][nc] != "#":
35                        dfs(nr, nc, node)
36
37            board[r][c] = char
38
39        for r in range(rows):
40            for c in range(cols):
41                dfs(r, c, trie)
42
43        return result