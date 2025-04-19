# Problem Link: https://leetcode.com/problems/count-the-number-of-fair-pairs/description/?envType=daily-question&envId=2025-04-19
# Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

# A pair (i, j) is fair if:

# 0 <= i < j < n, and
# lower <= nums[i] + nums[j] <= upper

#TC: O(N*LogN)

def lower_bound(nums, start, target):
    left = start
    right = len(nums) - 1
    ans = len(nums)
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

def upper_bound(nums, start, target):
    left = start
    right = len(nums) - 1
    ans = start - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n):
            min_val = lower - nums[i]
            max_val = upper - nums[i]
            l = lower_bound(nums, i + 1, min_val)
            r = upper_bound(nums, i + 1, max_val)
            count += max(0, r - l + 1)
        
        return count
        
