class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        key_stack = [0]
        rooms_visited = [0]*len(rooms)
        rooms_visited[0]=1
        while key_stack:
            k = key_stack.pop()
            if rooms_visited[k] == 0:
                rooms_visited[k]=1
            for new_key in rooms[k]:
                if rooms_visited[new_key]==0:
                    key_stack.append(new_key)
                    #stack.extend(rooms[k])
        for flag in rooms_visited:
            if flag==0:
                return False
        return True
