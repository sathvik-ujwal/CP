#Shortest Word Distance
'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
'''

class Solution:
    def shortest_distance(self, words: list[str], word1: str, word2: str) -> int:
        index = -1
        res = float('inf')
        last = ""
        
        for i,word in enumerate(words):
            if word == word1 or word == word2:
                if index != -1 and last != word:
                    res = min(res, i-index)
                index = i
                last = word 
                
        return res

sol = Solution()
words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "practice"
res = sol.shortest_distance(words, word1, word2)
print(res)


                    
                


