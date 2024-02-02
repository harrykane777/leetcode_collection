class Solution:
    def tribonacci(self, n: int) -> int:
        predest = []
        predest.append(0)
        predest.append(1)
        predest.append(1)
            
        for i in range(3, n + 1):
            predest.append(predest[i - 3] + predest[i - 2] + predest[i - 1])
        print(predest)
        return predest[n]
    
soln = Solution()
print(soln.tribonacci(4))