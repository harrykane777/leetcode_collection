class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        count = 0
        second = 0
        is_second = False
        record = []
        for num in nums:
            if num == 1:
                if is_second:
                    second += 1
                else:
                    count += 1
            else:
                if is_second:
                    count = second
                    second = 0
                is_second = True
            record.append(second + count)

        if len(record) == 0:
            return 0
        else:
            maxim = max(record)
            if maxim == len(nums):
                return maxim - 1
            return maxim

soln = Solution()
print(soln.longestSubarray([1,1,1]
))