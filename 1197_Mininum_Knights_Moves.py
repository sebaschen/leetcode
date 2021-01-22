import collections

class Solution:
    def minKnightMoves(self, s: int, e: int) -> int:
        #create a queue for saving the neighbors
        q = collections.deque()

        #put the starting point into queue
        q.append([0,0,0])

        #initialize the visited nodes
        visited = set()
        visited.add((0,0))


        # create BFS Loop
        # if queue is empty,stopped :
            # if x,y is equal to destination, stopped, return steps
            # else:
            # add directions to the current , if dirs not in visited, add the dir in queue, the current and steps add to queue
        while q:
            x,y,steps = q.popleft()
            if x == s and y == e:
                return steps
            dirs = [(x-1,y-2),(x-2,y-1),(x-2,y+1),(x-1,y+2),(x+1,y-2),(x+2,y-1),(x+1,y+2),(x+2,y+1)]
            for i,j in dirs:
                if (i,j) not in visited:
                    q.append([i,j,steps+1])
                    visited.add((i,j))
        return -1