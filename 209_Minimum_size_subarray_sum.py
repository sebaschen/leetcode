class Solution:
    def minSubArrayLen(self, the_sum: int, nums: List[int]) -> int:
        '''
        input type: the_sum:int, nums: List
        rtype: ans int 
        
        '''
        #fast, slow
        fast, slow = 0,0
        res = float(inf)
        N = len(nums)
        csum = 0
        
        while fast < N: #slow = 0, len(nums)= 6
            csum += nums[fast]
            while csum >= the_sum:
                res = min(res,fast-slow+1)
                csum -= nums[slow]
                slow+=1
            fast +=1             
        return res if res != float('inf') else 0
