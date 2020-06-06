class Solution:
    def convert(self, s: str, rows: int) -> str:
        # Consider Boundary case
        if rows ==1 or rows>len(s): return s        
        res = ["" for r in range(rows)]
        i,step = 0,0

        for ch in s:            
            res[i] +=ch    
            if i==0: #從第一列開始 first row
                step =1  #zigzag 往下走go down
            if i==rows -1 : #遇到最後一列last row
                step = -1 #往上走go up
            i+=step
            
        return "".join(res) #list to St