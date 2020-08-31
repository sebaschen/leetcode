class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque, max_deque = deque(), deque()
        l = r = 0
        ans = 0
        # [8,2,4,7]
        # 4
        while r < len(nums): #r= 3, len = 6 
            while min_deque and nums[r] <= nums[min_deque[-1]]: 
                min_deque.pop() #min_deque=[0] 
            while max_deque and nums[r] >= nums[max_deque[-1]]:
                max_deque.pop()             
            max_deque.append(r) #max_deque=[1,2,3]
            min_deque.append(r) #min_deque=[3] 
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                l += 1 #l=1
                print('l',l)
                if l > min_deque[0]:
                    min_deque.popleft()
                if l > max_deque[0]:
                    max_deque.popleft()
            
            ans = max(ans, r - l + 1)# ans = 2 
            r += 1  #r=2 
        
        return ans