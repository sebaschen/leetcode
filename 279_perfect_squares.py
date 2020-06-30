class Solution:
    def numSquares(self, n: int) -> int:
        '''
        input: int
        rtype: int
        Method: BFS, DP
        '''
        #boundary case
        if n < 2:
            return n
        
        #initiate the lst for all possible square numbers
        _list = []
        i = 1 ##
        while i**2 <=n:
            _list.append(i**2)  
            i+=1
        count = 0
        temp = {n}
        to_check = temp
        while to_check:
            count+=1
            temp =set()
            for x in to_check:
                for y in _list:
                    if x == y:
                        return count
                    if x>y:
                        temp.add(x-y)
            to_check = temp
        return count 
                        