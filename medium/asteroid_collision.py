class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            elif a < 0:
                if stack:
                    pos_a = stack.pop()
                    if pos_a * a > 0:
                        stack.append(pos_a)
                        stack.append(a)
                    elif -1 * a > pos_a:
                        broken = False
                        while stack:
                            temp = stack.pop()
                            if temp * a > 0: 
                                stack.append(temp)
                                break
                            if temp > -1 * a:
                                stack.append(temp)
                                broken = True
                                break
                            elif temp == -1 * a:
                                broken = True
                                break
                        if broken is False:
                            stack.append(a)
                    elif -1 * a < pos_a:
                        stack.append(pos_a)
                else:
                    stack.append(a)
        return stack
    
soln = Solution()
print(soln.asteroidCollision([-2,2,1,-2]))