# Problem Link:
# You are given an integer array nums. You need to ensure that the elements in the array are distinct. 
# To achieve this, you can perform the following operation any number of times:

# Remove 3 elements from the beginning of the array. If the array has fewer than 3 elements, remove all remaining elements.
# Note that an empty array is considered to have distinct elements. Return the minimum number of operations 
# needed to make the elements in the array distinct.

#TC : O(N)

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)

        for op in range(0,(n//3)+2):
            temp = nums[3*op:]
            
            if len(set(temp)) == len(temp):
                return op
        return (n+2)//3
