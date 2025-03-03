# Problem Link: https://leetcode.com/problems/partition-array-according-to-given-pivot/description/?envType=daily-question&envId=2025-03-03
# You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:

# Every element less than pivot appears before every element greater than pivot.
# Every element equal to pivot appears in between the elements less than and greater than pivot.
# The relative order of the elements less than pivot and the elements greater than pivot is maintained.
# More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. 
# If i < j and both elements are smaller (or larger) than pivot, then pi < pj.
# Return nums after the rearrangement.

#Approach 1:
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []           #stacks for storing the elments which are less than,equla to or greater than the pivot
        equal = []
        greater = []
        
        for ele in nums:
            if ele < pivot:
                less.append(ele)
            elif ele == pivot:
                equal.append(ele)
            else:
                greater.append(ele)
        rep = len(equal)
        ans = less+[pivot]*rep
        if(len(greater)>0):
            for i in greater:
                ans.append(i)

        return ans

#Approach 2 :
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # Get the length of the input array
        n = len(nums)
        
        # Create the result array of the same size
        result = [0] * n
        
        # Initialize pointers for filling the result array
        left_pointer = 0  # For elements less than pivot
        equal_count = 0   # Count elements equal to pivot
        
        # First pass: Count elements equal to pivot and place elements less than pivot
        for num in nums:
            if num < pivot:
                result[left_pointer] = num
                left_pointer += 1
            elif num == pivot:
                equal_count += 1
        
        # Second pass: Place all pivot elements
        right_pointer = left_pointer + equal_count  # Starting position for elements greater than pivot
        for i in range(equal_count):
            result[left_pointer + i] = pivot
        
        # Third pass: Place elements greater than pivot
        for num in nums:
            if num > pivot:
                result[right_pointer] = num
                right_pointer += 1
        
        return result
