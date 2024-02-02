def guess(num: int) -> int:
    if num < 6:
        return 1
    elif num > 6:
        return -1
    return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        def bin_search(lower, upper) -> int:
            search = (lower + upper) // 2
            num = guess(search)

            if num == -1:
                return bin_search(lower, search - 1)
            elif num == 1:
                return bin_search(search + 1, upper)
            else:
                return search
        return bin_search(1, n)
    
soln = Solution()
print(soln.guessNumber(10))