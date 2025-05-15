# Problem Link : https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/description/
# You are given a string array words and a binary array groups both of length n, where words[i] is associated with groups[i].

# Your task is to select the longest alternating subsequence from words. A subsequence of words is alternating if for any two consecutive strings in the sequence, their corresponding elements in the binary array groups differ. Essentially, you are to choose strings such that adjacent elements have non-matching corresponding bits in the groups array.

# Formally, you need to find the longest subsequence of an array of indices [0, 1, ..., n - 1] denoted as [i0, i1, ..., ik-1], such that groups[ij] != groups[ij+1] for each 0 <= j < k - 1 and then find the words corresponding to these indices.

# Return the selected subsequence. If there are multiple answers, return any of them.

# Note: The elements in words are distinct.

# TC : O(N)
# SC : O(N)

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        ans = [words[0]]
        last = groups[0]

        if n ==0 :
            return []
        for i in range(1,n):
            if groups[i] != last:
                ans.append(words[i])
                last = groups[i]
        return ans 
            
