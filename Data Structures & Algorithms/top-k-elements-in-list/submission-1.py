# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # seen = {}

        # for num in nums:

        #     if num in seen:
        #         seen[num] += 1
        #     else:
        #         seen[num] = 1

        # ans = []

        # while k > 0:

        #     maxi = -1
        #     number = None

        #     for key in seen:

        #         if seen[key] > maxi:
        #             maxi = seen[key]
        #             number = key

        #     ans.append(number)

        #     del seen[number]

        #     k -= 1

        # return ans
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for key in freq:
            bucket[freq[key]].append(key)

        ans = []

        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                ans.append(num)

                if len(ans) == k:
                    return ans