# Problem Link: https://leetcode.com/problems/partition-equal-subset-sum/description/?envType=daily-question&envId=2025-04-07
# Given an integer array nums, return true if you can partition the array into two subsets such
# that the sum of the elements in both subsets is equal or false otherwise.

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum%2 !=0:
            return False

        target = total_sum//2
        n = len(nums)

        dp = [False]*(target+1)
        dp[0] = True

        for num in nums:
            for i in range(target,num-1,-1):
                dp[i] = dp[i] or dp[i-num]
        
        return dp[target]
