class Solution:

    def maximumSum(self, nums: List[int]) -> int:
        d = {}
        max_sum = float('-inf')
        n = len(nums)

        def digit_sum(num):         #For calculating the sum of the digits of the number
            s = str(num)
            ans = 0
            for digit in s:
                ans += int(digit)
            return ans

        for i in range(n):          # checking and stroring the sum and index of the numbers
            temp = digit_sum(nums[i])
            if (temp in d.keys()):
                max_sum = max(max_sum,nums[i]+nums[d[temp]])
                if nums[i] > nums[d[temp]] :
                    d[temp] = i
            else:
                d[temp] = i
        if max_sum == float('-inf'):
            return -1
        
        return max_sum
