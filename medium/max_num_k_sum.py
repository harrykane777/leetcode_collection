class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        count = 0
        d = {}
        for num in nums:
            temp = k - num
            
            decrement = False
            if num in d:
                if d[num] > 0:
                    count += 1
                    d[num] -= 1
                    decrement = True
            
            if not decrement:
                if temp not in d:
                    d[temp] = 1
                else:
                    d[temp] += 1

            print(d, count)

        return count    
    

soln = Solution()
# [3,1,3,4,3], [1,2,3,4, 1, 5, 6, 7, 2, 5, 3]
# print(soln.maxOperations([4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4], 2))
print(soln.maxOperations([2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], 3))


# 1 3 3 3 4