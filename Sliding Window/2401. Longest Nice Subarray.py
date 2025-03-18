# Problem Link : https://leetcode.com/problems/longest-nice-subarray/description/?envType=daily-question&envId=2025-03-18
# You are given an array nums consisting of positive integers.
# We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.
# Return the length of the longest nice subarray.
# A subarray is a contiguous part of an array.
# Note that subarrays of length 1 are always considered nice.

# Time Complexity : O(N^2)
# space Complexity : O(1)

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        if n ==1:
            return n
        start =0
        end = 0
        size = 1

        while end<n-1 :
            end +=1
            is_valid = True
            
            for i in range(start,end):
                if nums[i] & nums[end] != 0:
                    is_valid = False
                    break

            if is_valid:
                size = max(size,end-start+1)
            else:
                start +=1
                end-=1
            
        return size
