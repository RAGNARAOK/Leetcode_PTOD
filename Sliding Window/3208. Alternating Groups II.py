# problem Link : https://leetcode.com/problems/alternating-groups-ii/description/?envType=daily-question&envId=2025-03-09
# There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

# colors[i] == 0 means that tile i is red.
# colors[i] == 1 means that tile i is blue.
# An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the f
# irst and last one has a different color from its left and right tiles).

# Return the number of alternating groups.

# Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        n = len(colors)
        N = n + (k - 1)

        # Handle wrap-around (circular array)
        colors.extend(colors[:k - 1])

        result = 0
        i = 0
        j = 1  # Because we need to check index j-1 for alternation

        while j < N:
            if colors[j] == colors[j - 1]:
                i = j
                j += 1
                continue

            if j - i + 1 == k:
                result += 1
                i += 1

            j += 1

        return result
