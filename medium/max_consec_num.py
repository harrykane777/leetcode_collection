from collections import deque
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:  
        flips = max_num = 0
        window = deque([])
        if k == 0:
            count = 0
            max_num = 0
            for i in range(len(nums)):
                if nums[i] == 1:
                    count += 1
                else:
                    count = 0
                if count > max_num:
                    max_num = count
            return max_num
                
        for i in range(len(nums)):
            if nums[i] == 1:
                window.append(nums[i])
            elif nums[i] == 0:
                if flips < k:
                    flips += 1
                    window.append(nums[i])
                else: 
                    while window:
                        if window.popleft() == 0:
                            break
                    window.append(nums[i])
            if len(window) > max_num:
                max_num = len(window)
        return max_num

soln = Solution()
print(soln.longestOnes([0,0,1,1,1,0,0], 0))
# 1, 1
# 1, 2
                