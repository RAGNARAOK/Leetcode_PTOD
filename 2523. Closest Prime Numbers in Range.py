# Problem Link : https://leetcode.com/problems/closest-prime-numbers-in-range/description/?envType=daily-question&envId=2025-03-07
# Given two positive integers left and right, find the two integers num1 and num2 such that:

# left <= num1 < num2 <= right .
# Both num1 and num2 are prime numbers.
# num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
# Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions,
# return the one with the smallest num1 value. If no such numbers exist, return [-1, -1]



from typing import List

class Solution:
    def isPrime(self, num: int) -> bool:
        if num == 1:  # Not a prime
            return False
        for div in range(2, int(num ** 0.5) + 1):
            if num % div == 0:
                return False
        return True

    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = []

        for num in range(left, right + 1):
            if self.isPrime(num):
                if primes and num - primes[-1] <= 2:
                    return [primes[-1], num]  # Early return
                
                primes.append(num)

        min_diff = float('inf')
        result = [-1, -1]

        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < min_diff:
                min_diff = diff
                result = [primes[i - 1], primes[i]]

        return result
