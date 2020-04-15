class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_record = 0 
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[zero_record] = nums[zero_record],nums[i]
                zero_record +=1
        