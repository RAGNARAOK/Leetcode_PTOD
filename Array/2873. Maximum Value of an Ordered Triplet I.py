# Probleml Link : https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/description/?envType=daily-question&envId=2025-04-02
# You are given a 0-indexed integer array nums.

# Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.

# The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].


# Appraoch 1 : Brute Force
# TC : O(N^3)

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = float("-inf")

        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    temp = (nums[i]-nums[j])*nums[k]
                    maxi = max(maxi,temp)

        if maxi<0:
            return 0
        return maxi


# Approach 2 linear way
# TC : O(N)

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_num = 0
        max_diff = float("-inf")
        result = 0

        for j in range(1,n):
            max_num = max(max_num,nums[j-1])

            max_diff = max(max_diff,max_num-nums[j])

            if j<n-1:
                result = max(result,max_diff*nums[j+1])
        if(result<0):
            return 0
        return result



