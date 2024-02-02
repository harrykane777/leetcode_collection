class Solution:
    def dailyTemperatures(self, temperatures):
        result = [0]
        stack = [len(temperatures) - 1]
        for i in range(len(temperatures) - 2, - 1, -1):
            popped = stack.pop()
            if temperatures[popped] > temperatures[i]:
                result.append(popped - i)
                stack.append(popped)
            else:
                did_reach = False
                while stack:
                    temp = stack.pop()
                    if temperatures[temp] > temperatures[i]:
                        result.append(temp - i)
                        did_reach = True
                        stack.append(temp)
                        break
                if not did_reach:
                    result.append(0)
                
            stack.append(i)
            
        return list(reversed(result))

soln = Solution()
print(soln.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))