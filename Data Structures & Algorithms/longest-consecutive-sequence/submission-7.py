class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        [-1,-1,0,1,2,3,4,5,6,7,8,9]
        if len(nums)==0:
            return 0
        else:
            nums.sort()
            c=1
            ans=1
            for i in range(len(nums)-1):
                if nums[i]+1==nums[i+1]:
                    c+=1
                elif nums[i]==nums[i+1]:
                    continue
                else:
                    c=1
                ans = max(ans, c)
        return ans
