# Problem Link : https://leetcode.com/problems/minimum-time-to-repair-cars/description/?envType=daily-question&envId=2025-03-16
# You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. 
# A mechanic with a rank r can repair n cars in r * n2 minutes.

# You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.

# Return the minimum time taken to repair all the cars.

# Note: All the mechanics can repair the cars simultaneously.






import math
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def is_possible(mid, cars):
            cars_fixed = 0
            for rank in ranks:
                cars_fixed += int(math.sqrt(mid / rank))
            return cars_fixed >= cars
    
        left = 1
        max_rank = max(ranks)
        right = max_rank * cars * cars
        result = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            if is_possible(mid, cars):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return result
