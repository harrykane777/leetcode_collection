class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [nums[0]]
        if len(nums) > 1 and nums[1] > nums[0]:
            dp.append(nums[1])
        else:
            dp.append(nums[0])
        for i in range(2, len(nums)):
            if nums[i] + dp[i - 2] > dp[i - 1]:
                dp.append(nums[i] + dp[i - 2])
            else:
                dp.append(dp[i - 1])

        return dp[-1]
    
soln = Solution()
print(soln.rob([]))