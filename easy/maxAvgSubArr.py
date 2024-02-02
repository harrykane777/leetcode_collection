
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        nums_len = len(nums)
        initial = 0.0
        for j in range(0, k):
            if k <= nums_len:
                initial += nums[j]
        real = initial / k

        for i in range(1, nums_len):
            if i + k <= nums_len:
                initial = initial - nums[i - 1] + nums[i + k - 1]
            if initial / k > real:
                real = initial / k 

        return real

soln = Solution()
print(soln.findMaxAverage([1,12,-5,-6,50,3], 4))