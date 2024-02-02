from queue import Queue

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_list = Queue()
        d_list = Queue()

        n = len(senate)
        for i in range(n):
            if senate[i] == "R":
                r_list.put(i)
            elif senate[i] == "D":
                d_list.put(i)
        
        while not r_list.empty() and not d_list.empty():
            r = r_list.get()
            d = d_list.get()
                        
            if r > d:
                d_list.put(d + n)
            else:
                r_list.put(r + n)
                    
        return "Radiant" if d_list.empty() else "Dire"
soln = Solution()
print(soln.predictPartyVictory("DRDRR"))