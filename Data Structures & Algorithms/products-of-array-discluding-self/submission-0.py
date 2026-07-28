class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right=[1]*len(nums)
        prod_right=1
        prod_left=1
        left=[1]*len(nums)
        final=[]
        for i in range(len(nums)-1,-1,-1):
            right[i]=prod_right
            prod_right*=nums[i]
        for i in range(len(nums)):
            left[i]=prod_left
            prod_left*=nums[i]
        for i in range(len(nums)):
            final.append(left[i]*right[i])
        return final
            

