class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        s_len = len(s)
        max_vowel = 0
        for i in range(k):
            if s[i] == "a" or s[i] == "e" \
                or s[i] == "i" or s[i] == "o" \
                or s[i] == "u":
                max_vowel += 1
        temp = max_vowel

        j = 0
        for i in range(k, s_len):
            temp_max = temp
            first = s[j]
            if first == "a" or first == "e" \
                or first == "i" or first == "o" \
                or first == "u":
                temp_max -= 1

            if s[i] == "a" or s[i] == "e" \
                or s[i] == "i" or s[i] == "o" \
                or s[i] == "u":
                temp_max += 1
            if temp_max > max_vowel:
                max_vowel = temp_max
            temp = temp_max
            j += 1
            
        return max_vowel


soln = Solution()
print(soln.maxVowels("leetcode", 3))