class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        fin=[]
        m=len(nums1)
        n=len(nums2)
        i=0
        j=0
        while i <m and j<n:
            if nums1[i]<nums2[j]:
                fin.append(nums1[i])
                i+=1
            else:
                fin.append(nums2[j])
                j+=1
        fin.extend(nums1[i:])
        fin.extend(nums2[j:])
        l=len(fin)
        if len(fin)%2!=0:
            med=fin[l//2]
        else:
            med=(fin[(l//2-1)]+fin[l//2])/2
        return med
