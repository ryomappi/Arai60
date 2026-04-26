from collections import deque


class Solution:
    def getHammingDistance(self, str1, str2):
        if len(str1) != len(str2):
            raise ValueError
        n = len(str1)
        distance = 0
        for i in range(n):
            if str1[i] != str2[i]:
                distance += 1
        return distance

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        allWords = [beginWord] + wordList
        n = len(allWords)
        end_idx = allWords.index(endWord)
        # Adjacent list
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if self.getHammingDistance(allWords[i], allWords[j]) == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        # BFS
        visited = [False] * n
        visited[0] = True
        dq = deque([(0, 1)])  # (index, #words)

        while dq:
            idx, count = dq.popleft()
            if idx == end_idx:
                return count
            for neighbor in graph[idx]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dq.append((neighbor, count + 1))
        return 0
    