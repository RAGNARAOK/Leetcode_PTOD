# Problem Link :
# Given an integer array nums and an integer k, return the number of good subarrays of nums.

# A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

# A subarray is a contiguous non-empty sequence of elements within an array.

#TC: O(N)
#SC: O(N)

from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        left = 0    
        freq = defaultdict(int)
        count = 0 
        pairs = 0
        
        for right in range(n):
            pairs += freq[nums[right]]
            freq[nums[right]] +=1

            while pairs >=k:
                count += (n-right)
                freq[nums[left]] -= 1
                pairs -= freq[nums[left]]
                left+=1
        return count
