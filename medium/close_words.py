from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1 = Counter(word1)
        w2 = Counter(word2)
        if w1.keys() != w2.keys():
            return False
                    
        return Counter(w1.values()) == Counter(w2.values())

    
soln = Solution()
print(soln.closeStrings("abc", "bca"))