class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        1. Iterate over all the elements in nums.
        2. If some number in nums is new to array, append it.
        3. If some number is already in the array, remove it.
        '''
        #create new list
        new_list=[]
        for i in nums:
            if i not in new_list:
                new_list.append(i)
            else:
                new_list.remove(i)                     
        return new_list.pop()