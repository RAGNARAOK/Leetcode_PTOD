# Problem Link : https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/
# You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies 
# of size candies[i]. You can divide each pile into any number of sub piles, but you cannot merge two piles together.
# You are also given an integer k. You should allocate piles of candies to k children such that each 
# child gets the same number of candies. Each child can be allocated candies from only one pile of candies
# and some piles of candies may go unused.
# Return the maximum number of candies each child can get.

#Approach 1 -- Bruteforce
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        maxc = max(candies) 
        n = len(candies)
        c = maxc
        while c>=1:
            count = 0
            for i in range(n):
                count += candies[i]//c
            if count>=k:
                return c
            c-=1
        return 0
# Approach 2 Using Binary Search
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if not candies or sum(candies)<k:
            return 0
        left = 1
        right = max(candies)

        while left<=right:
            mid = left + (right-left)//2
            count = sum(piles//mid for piles in candies)

            if count>=k :
                left = mid+1
            else:
                right = mid -1
        return right
