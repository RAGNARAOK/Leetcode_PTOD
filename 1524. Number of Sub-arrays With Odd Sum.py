# problrm link: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description/?envType=daily-question&envId=2025-02-25

# Given an array of integers arr, return the number of subarrays with an odd sum.

# Since the answer can be very large, return it modulo 109 + 7.

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = 0
        odd = 0
        even = 0
        csum = 0
        for num in arr:
            csum+=num
            if csum%2:
                res+=1+even
                odd+=1
            else:
                res+=odd
                even+=1
        return res%(10**9+7)