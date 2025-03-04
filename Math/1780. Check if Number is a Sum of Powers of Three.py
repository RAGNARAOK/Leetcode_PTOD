# problem Link : https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/description/?envType=daily-question&envId=2025-03-04
# Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

# An integer y is a power of three if there exists an integer x such that y == 3x.

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
         
        if n == 3:
            return True
        while n>0:
            rem = n%3
            if rem == 2:
                return False
            n //=3
        return True

# The solution works by checking if n can be written in base 3 without using the digit 2. We repeatedly divide n by 3 and check if any remainder is 2. If we find a remainder of 2, it means we can't represent the number as a sum of distinct powers of three.
# For example:

# For n = 12:

# 12 ÷ 3 = 4 remainder 0
# 4 ÷ 3 = 1 remainder 1
# 1 ÷ 3 = 0 remainder 1
# So 12 in base 3 is 110, which corresponds to 1×3^2 + 1×3^1 + 0×3^0 = 9 + 3 = 12
# Since all digits are 0 or 1, return true

# For n = 21:

# 21 ÷ 3 = 7 remainder 0
# 7 ÷ 3 = 2 remainder 1
# 2 ÷ 3 = 0 remainder 2
# Since we have a remainder of 2, return false

# The time complexity is O(log n) since we're doing at most log₃(n) divisions.
 
