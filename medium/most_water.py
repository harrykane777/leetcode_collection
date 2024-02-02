class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        i = 0
        j = len(height) - 1
        while i != j:
            area = min(height[i], height[j]) * abs(j - i)
            print(area)
            if area > max_area:
                max_area = area

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_area
    
soln = Solution()
print("Max: " + str(soln.maxArea([1,3,2,5,25,24,5])))