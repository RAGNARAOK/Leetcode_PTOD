# Problem Link : https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/
# Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

# In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
# Note that 0 is neither positive nor negative.

#---------------------------------------------------------------------------Approach 1 ------------------------------------------------------------------------------------------
#TC : O(log N)

class Solution:

    def upperbound(self,nums):
        start = 0
        end = len(nums)-1
        index = len(nums)
        while start<=end:
            mid = (start+end)//2
            if nums[mid]<=0:
                start = mid+1
            else :
                end = mid -1
                index = mid

        return index
    
    def lowerbound(self,nums):
        start = 0
        end = len(nums)-1
        index = len(nums)
        while start<=end:
            mid = (start+end)//2
            if nums[mid]<0:
                start = mid+1
            else :
                end = mid -1
                index = mid

        return index

    
    def maximumCount(self, nums: List[int]) -> int:
        positive_count = len(nums) - self.upperbound(nums)

        negative_count = self.lowerbound(nums)

        return max(positive_count,negative_count)

#-------------------------------------------------------------------------------Approach 2---------------------------------------------------------------------------------
# TC : O(N)
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        neg = 0
        pos = 0
        for i in nums:
            if i>0:
                pos+=1
            elif i<0:
                neg+=1
            else:
                pass

        return max(pos,neg)
