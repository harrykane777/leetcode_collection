import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]
    
soln = Solution()
print(soln.findKthLargest([3,2,1,5,6,4], 2))