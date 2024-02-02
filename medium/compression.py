class Solution:
    def compress(self, chars: list[str]) -> int:
        s = ""
        consec = ""
        chars_len = len(chars)

        for i in range(0, chars_len):
            if len(consec) == 0 or consec[0] == chars[i]:
                consec += chars[i]
            if i == chars_len - 1 or consec[0] != chars[i]:
                s += consec[0]
                if len(consec) > 1:
                    s += str(len(consec))
                if chars_len - 1 == i and chars[i] != consec[0]:
                    s += chars[i]
                consec = chars[i]

        for i in range(chars_len):
            if i < len(s):
                chars[i] = s[i]
            else:
                chars.pop()
        return len(chars)
    
soln = Solution()
print(soln.compress(["a","b","c"]))