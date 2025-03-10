# Problem Link : https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description/?envType=daily-question&envId=2025-03-10
# You are given a string word and a non-negative integer k.

# Return the total number of substrings of word that 
# contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

class Solution:
    def is_vowel(self, ch: str) -> bool:
        return ch in {'a', 'e', 'i', 'o', 'u'}
    
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        
        # Dictionary to keep count of vowels in the current window
        vowel_count = {}  # Equivalent to unordered_map<char, int> in C++
        
        # Preprocessing to find the next consonant index
        next_cons = [n] * n  # Initialize with n (out of bounds index)
        last_cons_idx = n
        
        # Traverse from right to left to store the next consonant's index
        for i in range(n - 1, -1, -1):
            next_cons[i] = last_cons_idx
            if not self.is_vowel(word[i]):  # If it's a consonant
                last_cons_idx = i
        
        i, j = 0, 0
        count = 0
        cons = 0  # Consonant count
        
        # Sliding window technique
        while j < n:
            ch = word[j]
            if self.is_vowel(ch):
                vowel_count[ch] = vowel_count.get(ch, 0) + 1
            else:
                cons += 1  # Count consonants
            
            # Ensure the window has exactly 'k' consonants
            while cons > k:
                ch = word[i]
                if self.is_vowel(ch):
                    vowel_count[ch] -= 1
                    if vowel_count[ch] == 0:
                        del vowel_count[ch]
                else:
                    cons -= 1
                i += 1

            # If all 5 vowels exist in the window and cons == k, count valid substrings
            while i < n and len(vowel_count) == 5 and cons == k:
                idx = next_cons[j]  # Next consonant index after j
                count += idx - j  # Main logic for counting substrings
                
                ch = word[i]
                if self.is_vowel(ch):
                    vowel_count[ch] -= 1
                    if vowel_count[ch] == 0:
                        del vowel_count[ch]
                else:
                    cons -= 1
                i += 1
            
            j += 1

        return count
