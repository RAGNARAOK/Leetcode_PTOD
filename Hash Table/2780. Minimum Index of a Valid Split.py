# Problem Link :https://leetcode.com/problems/minimum-index-of-a-valid-split/description/
# An element x of an integer array arr of length m is dominant if more than half the elements of arr have a value of x.

# You are given a 0-indexed integer array nums of length n with one dominant element.

# You can split nums at an index i into two arrays nums[0, ..., i] and nums[i + 1, ..., n - 1], but the split is only valid if:

# 0 <= i < n - 1
# nums[0, ..., i], and nums[i + 1, ..., n - 1] have the same dominant element.
# Here, nums[i, ..., j] denotes the subarray of nums starting at index i and ending at index j, both ends being inclusive.
# Particularly, if j < i then nums[i, ..., j] denotes an empty subarray.

# Return the minimum index of a valid split. If no valid split exists, return -1.

#TC: O(N)
#SC: O(N)
'''
Intuition
Find the most frequent element (dominant)
Try to split the array such that:

Left part has dominant element > left part length/2
Right part has dominant element > right part length/2

Approach
Find the dominant (most frequent) element in the entire array
Iterate through the array to find the first valid split point
For each index, check two conditions:

Dominant element count in left subarray > left length/2
Dominant element count in right subarray > right length/2

Return the first index that satisfies these conditions
If no such index exists, return -1
'''
from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        freq = Counter(nums)
        dominant = max(freq, key=freq.get)
        
        total_dominant_count = freq[dominant]
        left_count = 0
        
        for j in range(len(nums)):    
            if nums[j] == dominant:
                left_count += 1  
            left_length = j + 1
            right_length = len(nums) - left_length
             
            if (left_count > left_length // 2) and \
               (total_dominant_count - left_count > right_length // 2):
                return j
        
        return -1
