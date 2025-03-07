# leetcode 127 
'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList 
is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words 
in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
'''

from collections import defaultdict
from typing import List
# dfs (TLE)
# O(n^2*m)

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        graph = defaultdict(list)

        def checkword(word1, word2):
            cnt = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    cnt += 1

                    if cnt == 2:
                        return False

            return True

        added =set()
        wordList.append(beginWord)
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                if checkword(wordList[i], wordList[j]) and  (wordList[i], wordList[j]) not in added:
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])

                added.add((wordList[i], wordList[j]))
        self.res = float('inf')
        self.visited =set()

        def dfs(word, cnt, par):
            if word == endWord:
                self.res=min(self.res, cnt)
                return 
            if word in self.visited:
                return

            self.visited.add(word)
            for neigh in graph[word]:
                if neigh == par:
                    continue
                dfs(neigh, cnt+1, word)
            self.visited.remove(word)
            return

        dfs(beginWord, 1, "")
        return self.res if self.res != float('inf') else 0
                

                
# bfs with additional optimization in checking strings 
# O(m^2*n)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
       
        graph = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                graph[pattern].append(word)

        visited = set()
        visited.add(beginWord)
        q = deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]

                    for neigh in graph[pattern]:
                        if neigh not in visited:
                            visited.add(neigh)
                            q.append(neigh)
            res += 1

        return 0
