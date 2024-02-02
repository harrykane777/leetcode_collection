# LeetCode 841, DFS

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = [False for i in range(len(rooms))]
        visited[0] = True
        def depthFirstSearch(rooms, room_num):
            print(room_num)
            keys = rooms[room_num]
            for key in keys:
                if visited[key] is False:
                    visited[key] = True
                    depthFirstSearch(rooms, key)
                
        depthFirstSearch(rooms, 0)
        for v in visited:
            if not v:
                return False
        return True
    
soln = Solution()
print(soln.canVisitAllRooms( [[1,3],[3,0,1],[2],[0]]))