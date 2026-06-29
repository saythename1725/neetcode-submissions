class Solution:
    #brute force t:o(n^2) s:o(n)
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     n=len(nums)
    #     for i in range(n):
    #         for j in range(i+1,n):
    #             if nums[i]==nums[j]:
    #                 return True
    #     return False    
    def hasDuplicate(self, nums: List[int]) -> bool:
        #optimzied t:o(n) s:o(n)
        seen =set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])
        return False     
