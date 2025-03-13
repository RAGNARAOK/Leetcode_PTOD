# Problem Link : https://leetcode.com/problems/zero-array-transformation-ii/description/?envType=daily-question&envId=2025-03-13
# You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].

# Each queries[i] represents the following action on nums:

# Decrement the value at each index in the range [li, ri] in nums by at most vali.
# The amount by which each value is decremented can be chosen independently for each index.
# A Zero Array is an array with all its elements equal to 0.

# Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.

#TC:  O(Q² + Qn)
#But this approach will throw TLE

 class Solution:
    def checkWithDifferenceArrayTeq(self, nums, queries, k):
        n = len(nums)
        diff = [0] * n

        # O(k)
        for i in range(k + 1):
            l, r, x = queries[i]
            diff[l] += x
            if r + 1 < n:
                diff[r + 1] -= x

        cumSum = 0
        # O(n)
        for i in range(n):
            cumSum += diff[i]
            diff[i] = cumSum

            if nums[i] - diff[i] > 0:  # If nums[i] can't become 0
                return False

        return True

    def minZeroArray(self, nums, queries):
        n = len(nums)
        Q = len(queries)

        # If all elements are already 0, return 0
        if all(x == 0 for x in nums):
            return 0

        # Brute force to find the minimum number of queries
        for i in range(Q):
            if self.checkWithDifferenceArrayTeq(nums, queries, i):
                return i + 1
        
        return -1
#---------------------------------------------------------------------------------Approach 2 --------------------------------------------------------------------------------
#TC: O(Q*n*log.Q)

class Solution:
    def checkWithDifferenceArrayTeq(self, nums, queries, k):
        n = len(nums)
        diff = [0] * n

        # Apply first k queries
        for i in range(k + 1):
            l, r, x = queries[i]
            diff[l] += x
            if r + 1 < n:
                diff[r + 1] -= x

        # Calculate prefix sum of the difference array
        cumSum = 0
        for i in range(n):
            cumSum += diff[i]
            if nums[i] - cumSum > 0:  # If nums[i] can't become zero
                return False

        return True

    def minZeroArray(self, nums, queries):
        n = len(nums)
        Q = len(queries)

        # Edge case: If all elements are already zero
        if all(x == 0 for x in nums):
            return 0

        # Binary Search for minimum `k`
        left, right = 0, Q - 1
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            if self.checkWithDifferenceArrayTeq(nums, queries, mid):
                ans = mid + 1  # Store the current valid answer
                right = mid - 1  # Try for a smaller k
            else:
                left = mid + 1  # Increase the range
        
        return ans
