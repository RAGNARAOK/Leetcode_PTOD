# Problem Link : https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/?envType=daily-question&envId=2025-03-11
# Given a string s consisting only of characters a, b and c.

# Return the number of substrings containing at least one occurrence of all these characters a, b and c.
# TC: O(N)
# SC: O(1)

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        result = 0
        
        counts = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        
        for right in range(n):
            
            if s[right] in counts:
                counts[s[right]] += 1
            
            while left <= right and all(counts[char] > 0 for char in 'abc'):
                result += n - right
               
                if s[left] in counts:
                    counts[s[left]] -= 1
                left += 1
        
        return result
