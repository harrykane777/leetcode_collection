class Solution:
    def check_gcd(self, potential_div, str1, str2, len_1, len_2) -> str:
        len_divisor = len(potential_div)

        if len_divisor == 0:
            return ""
        
        track = 0
        for j in range(len_1):
            if len_divisor > 0 and str1[j] ==potential_div[track]:
                track += 1
            else:
                potential_div.pop()
                return self.check_gcd(potential_div, str1, str2, len_1, len_2)

            if track >= len_divisor:
                track = 0
        
        if track != 0:
            potential_div.pop()
            return self.check_gcd(potential_div, str1, str2, len_1, len_2)

        track = 0
        for j in range(len_2):
            if len_divisor > 0 and str2[j] == potential_div[track]:
                track += 1
            else:
                potential_div.pop()
                return self.check_gcd(potential_div, str1, str2, len_1, len_2)

            if track >= len_divisor:
                track = 0
        
        if track != 0:
            potential_div.pop()
            return self.check_gcd(potential_div, str1, str2, len_1, len_2)

        return "".join(potential_div)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        i = 0
        my_potential_div = []
        len_1 = len(str1)
        len_2 = len(str2)

        while i < len_1 and i < len_2 and str1[i] == str2[i]:
            my_potential_div.append(str1[i])
            i += 1

        return self.check_gcd(my_potential_div, str1, str2, len_1, len_2)
    



test = Solution()
print(test.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))