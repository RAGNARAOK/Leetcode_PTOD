# Problem Link : https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/?envType=daily-question&envId=2025-03-08
# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 
# 'W' and 'B' denote the colors white and black, respectively.
# You are also given an integer k, which is the desired number of consecutive black blocks.
# In one operation, you can recolor a white block such that it becomes a black block.
# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.



class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        black_count = 0
        ans = float("inf")
        for i in range(len(blocks)):
            if i - k >= 0 and blocks[i - k] == 'B': 
                black_count -= 1
            if blocks[i] == 'B':
                black_count += 1            
            ans = min(ans, k - black_count)
        
        return ans
