class Solution:
    def reverseVowels(self, s: str) -> str:
        length = len(s)
        i = -1 
        vowel_list = []
        s = list(s)
        vowel_indices = []
        for ch in s:
            if (s[i] == "a" or s[i] == "e" or  s[i] == "i" or s[i] == "o" or s[i]== "u") or \
            (s[i] == "A" or s[i] == "E" or s[i] == "I" or s[i] == "O" or s[i]== "U"):
                vowel_list += s[i]
                vowel_indices.append(length + i)
            i += -1

        vowel_indices.sort()
        i = 0
        for indice in vowel_indices:
            s[indice] = vowel_list[i]
            i += 1

        return "".join(s)
    

new = Solution()
print(new.reverseVowels("leetcode"))