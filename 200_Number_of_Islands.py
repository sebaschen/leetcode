#200. Number of Islands
#200_Number_of_Islands.py
# Time complexity O(mn)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        For every land, visit its neighborland
        using DFS until there's no such land mark every visited nodes to 0 
        """        
        
        #initialization
        m = len(grid) #m 是列數
        if m == 0: return 0
        n = len(grid[0]) #n是行數
        ans = 0
        for y in range(m):
            for x in range(n):
                if grid[y][x] == '1':
                    ans += 1                                        
                    self.__dfs(grid, x, y, n, m)
        return ans
    
    def __dfs(self, grid, x, y, n, m):
        if x < 0 or y < 0 or x >=n or y >= m or grid[y][x] == '0':
            return None  #return none 會繼續跑下行程式
        #走過的Node即改成0,視為已經踩過
        grid[y][x] = '0'
        
        #以原點開始上下左右traverse through, 只能左右走或是上下走
        self.__dfs(grid, x + 1, y, n, m)
        self.__dfs(grid, x, y + 1, n, m)
        self.__dfs(grid, x, y - 1, n, m)
        self.__dfs(grid, x - 1, y, n, m)
        