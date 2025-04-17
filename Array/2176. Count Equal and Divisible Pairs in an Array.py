# Problem Link :https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/description/
# Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j)2
# where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.

# TC:O(N^2)
# SC:O(1)

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            for j in range(i+1,n):
                if nums[i] == nums[j] and (i*j)%k ==0:
                    count+=1
        return count
            
