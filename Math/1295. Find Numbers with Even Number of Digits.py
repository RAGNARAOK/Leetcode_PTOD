# Problem Link : 
# Given an array nums of integers, return how many of them contain an even number of digits.

# Approach 1
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for num in nums if (num >= 10 and num < 100) or 
                                        (num >= 1000 and num < 10000) or 
                                        num == 100000)

# Approach 2
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            temp = str(num)
            str_len = len(temp)
            if str_len%2 == 0:
                count+=1
        return count
