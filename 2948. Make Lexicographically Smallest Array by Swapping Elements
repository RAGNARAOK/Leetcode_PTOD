from typing import List
from collections import defaultdict, deque

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        # Create a sorted copy of nums
        vec = sorted(nums)

        group_num = 0
        num_to_group = {}
        group_to_list = defaultdict(deque)

        # Initialize the first element's group
        num_to_group[vec[0]] = group_num
        group_to_list[group_num].append(vec[0])

        for i in range(1, n):
            # If the difference exceeds the limit, start a new group
            if abs(vec[i] - vec[i - 1]) > limit:
                group_num += 1
            
            num_to_group[vec[i]] = group_num
            group_to_list[group_num].append(vec[i])

        # Build the answer by merging groups
        result = []
        for num in nums:
            group = num_to_group[num]
            # Get the smallest available number in this group
            result.append(group_to_list[group].popleft())

        return result
