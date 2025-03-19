# Problem Link : https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/
# You are given a binary array nums.

# You can do the following operation on the array any number of times (possibly zero):

# Choose any 3 consecutive elements from the array and flip all of them.
# Flipping an element means changing its value from 0 to 1, and from 1 to 0.

# Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.

# Time Complexity : O(N)
# Space Complexity : O(1) 

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums) 
        op = 0

        for i in range(n-2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                op+=1
        if (sum(nums)==n):
            return op
        return -1
