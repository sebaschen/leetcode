#525. Contiguous Array
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''
        check if the current sum has the same before, if same sum index now - previous index.
        To get the previous index, we save it as: table[count]=index
    
        '''
        count = 0
        max_length=0
        table = {0: 0}
        for index, num in enumerate(nums,1):#remember, index starts at 1
            if num ==0:
                count-=1
            elif num == 1:
                count+=1
            if count in table:
                max_length = max(max_length,index-table[count])
            else:
                table[count]=index
        return max_length