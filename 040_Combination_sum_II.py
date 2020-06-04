class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #consider boundary case:
        res =[]
        if len(candidates)==0:
            return []
        self.dfs(candidates,target,0,[],res)
        return res
    
    def dfs(self, nums, target, index, path, res):                
        if target < 0:
            return
        if target ==0:
            path = sorted(path)
            if path in res:
                return
            else:
                res.append(path)
                return res
        for i in range(index,len(nums)):
            self.dfs(nums[1:],target-nums[i],i,path+[nums[i]],res)
            
        