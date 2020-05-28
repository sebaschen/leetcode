class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    
        #Flood fill 指的是 Starting point 的上下左右是否為1如果是的話，改成Color，
        #類似題：200. Number of Islands

        #initialization
        SR = len(image)
        SC = len(image[0])
        color = image[sr][sc]
        
        if color == newColor: return image
        def __dfs(r,c):
            if image[r][c] == color:
                image[r][c]= newColor
                if c >=1: __dfs(r,c-1)
                if r >=1: __dfs(r-1,c)
                if c < SC-1: __dfs(r,c+1)
                if r < SR-1: __dfs(r+1,c)
        __dfs(sr,sc)
        return image
                