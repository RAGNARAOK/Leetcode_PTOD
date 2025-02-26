# Problem Link: https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/?envType=daily-question&envId=2025-02-26
# You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

# Return the maximum absolute sum of any (possibly empty) subarray of nums.

# Note that abs(x) is defined as follows:

# If x is a negative integer, then abs(x) = -x.
# If x is a non-negative integer, then abs(x) = x.

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        s = list(accumulate(nums, initial=0))
        return max(s) - min(s)


# ------------------------------------------------------------------------Approach-------------------------------------------------------------------------------------------
# This solution uses prefix sums (also called cumulative sums) to solve the problem in a surprisingly simple way. 
# The accumulate function from the itertools module calculates a running sum of the elements.
# Here's a step-by-step explanation of how this works:
# First, let's understand what s = list(accumulate(nums, initial=0)) does:

# It creates a list of prefix sums, starting with 0
# For nums = [2,-5,1,-4,3,-2], the prefix sums would be:

# s = [0, 2, -3, -2, -6, -3, -5]
# Each element represents the sum of all numbers up to that point



# Now, the key insight: the sum of any subarray nums[i:j+1] can be calculated as s[j+1] - s[i].
# For example, to get the sum of subarray [-5,1,-4], we would calculate:

# This subarray starts at index 1 and ends at index 3
# Sum = s[4] - s[1] = -6 - 2 = -8

# To find the maximum absolute sum, we need the maximum possible value of |s[j] - s[i]| where j > i.
# This expression is maximized when we have the largest possible difference between any two elements in the prefix sum array. 
#   This happens when we take the maximum value in the array and subtract the minimum value.
# Hence: max(s) - min(s)
# For our example:

# max(s) = 2 (the largest prefix sum)
# min(s) = -6 (the smallest prefix sum)
# max(s) - min(s) = 2 - (-6) = 8

# This is exactly the maximum absolute sum we found using the Kadane-based approach!
