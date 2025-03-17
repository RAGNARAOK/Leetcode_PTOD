# Problem Link:https://leetcode.com/problems/divide-array-into-equal-pairs/description/
# You are given an integer array nums consisting of 2 * n integers.

# You need to divide nums into n pairs such that:

# Each element belongs to exactly one pair.
# The elements present in a pair are equal.
# Return true if nums can be divided into n pairs, otherwise return false.

# Approach 1:
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # If the array length is odd, it's impossible to divide into pairs
        if len(nums) % 2 != 0:
            return False
        
        # Count occurrences of each number
        cnt_map = {}
        for num in nums:
            cnt_map[num] = cnt_map.get(num, 0) + 1
        
        # Check if all numbers appear an even number of times
        for count in cnt_map.values():
            if count % 2 != 0:
                return False
        
        return True
  # Approach 2:
  class Solution:
    def divideArray(self, nums: List[int]) -> bool:
         
        cnt = len(nums)
        if cnt % 2 != 0:  
            return False
            
        cnt_map = {}
        counter = 0

        for ele in nums:
            if ele in cnt_map:  
                cnt_map.pop(ele)
                counter += 1
            else:
                cnt_map[ele] = 1  
        
        # Check if all elements were paired
        if len(cnt_map) == 0:  cnt/2
            return True
        return False
