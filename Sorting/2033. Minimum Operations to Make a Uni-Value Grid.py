# Problem Link: https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/description/?envType=daily-question&envId=2025-03-26
# You are given a 2D integer grid of size m x n and an integer x. In one operation, 
# you can add x to or subtract x from any element in the grid.

# A uni-value grid is a grid where all the elements of it are equal.

# Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

# TC : O(NLogN)
# SC : O(N)
'''
Intuition
The key insight is to use the median as the target value because it minimizes the total number of 
operations required to equalize all elements. This works because the median minimizes the sum of absolute deviations.
Additionally, all elements must have the same remainder when divided by x for a valid solution to exist.

Approach
Flatten the Grid: Convert the 2D grid into a 1D list for easier processing.

Sort the List: Sorting helps identify the median(s) efficiently.

Check Valid Targets:

For an odd-length list, check the middle element (median).

For an even-length list, check both middle elements to account for two potential medians.

Validate Divisibility:

For each candidate target, ensure all elements can reach it by verifying that their differences are multiples of x.

If any element cannot reach the target, the problem has no solution.

Calculate Operations:

Sum the minimum steps (difference // x) for valid targets.

Return the minimum steps between valid candidates or -1 if no solution exists.
'''
def solver(nums,target,x):
    op = 0
    for ele in nums:
        diff = abs(target - ele)
        if(diff%x!=0):
            return -1
            break
        else:
            op += diff//x
    return op


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []

        for row in grid:
            nums.extend(row)

        nums.sort()
        n = len(nums)

        target1 = float("inf")
        target2 = float("inf")

        if(n%2==0):
            target1 = solver(nums,nums[n//2],x)
            target2 = solver(nums,nums[(n//2)-1],x)

        else:
            target1 = solver(nums,nums[n//2],x)
        
        return min(target1,target2)
        

        
