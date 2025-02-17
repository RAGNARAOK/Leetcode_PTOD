# You have n  tiles, where each tile has one letter tiles[i] printed on it.
# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.
# Leetcode problem number 1079
from collections import Counter
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter = Counter(tiles)    #using counter function to store the frequency of each element of the string 
        
        def dfs(counter):       # Recursive code 
            total = 0
            for tile,cnt in counter.items():
                if cnt > 0:
                    counter[tile] -=1   # fill one tail and try for the all the permutations 
                    total +=1
                    total +=dfs(counter)
                    counter[tile] +=1   # backtrack to see with other char as starting element
            return total
        ans = dfs(counter)
        return ans
    
