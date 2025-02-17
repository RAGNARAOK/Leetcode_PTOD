from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums):
        n = len(nums)
        tuples = 0

        product_count = defaultdict(int)  # Dictionary to store product frequency

        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1

        for freq in product_count.values():
            tuples += (freq * (freq - 1)) // 2  # Choosing two pairs

        return tuples * 8  # Each combination contributes to 8 valid tuples
