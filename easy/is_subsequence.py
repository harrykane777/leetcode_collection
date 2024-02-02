class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tracker = 0
        s_len = len(s)
        for i in range(len(t)):
            if tracker < s_len and t[i] == s[tracker]:
                tracker += 1

        if tracker == s_len:
            return True
        return False


soln = Solution()
print(soln.isSubsequence("", "ahbgdc"))