#30 days leetcode challenge
#Week 2 day 7
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        '''
        1. sum the total left steps and right steps
        2. only move the remainder of the len(string)
        '''
        sum = 0
        for i in range(len(shift)):            
            if shift[i][0] ==0:
                sum -= shift[i][1]                 
            elif shift[i][0]==1:    
                #right
                sum += shift[i][1]
        sum = sum%len(s)
        if sum == 0:
            return s
        else:
            return s[-sum:] + s[:-sum]
       