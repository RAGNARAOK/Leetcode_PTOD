# Approach 1 : Cantor's Diagonal argument method
# Time complexity : O(N)
# Space complexity : O(1) 
# Detailed explanation of this method : https://leetcode.com/problems/find-unique-binary-string/solutions/6446034/on-approach-using-cantors-diagonal-argum-ovxt

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ''
        n = len(nums) 

        for i in range(n):

            ans+='1' if nums[i][i] == '0' else '0'
        return ans

#---------------------------------------------------------------------------------------------------------------------------------
# Approach 2 : Backtracking
# Time complexity : O(N82^N)

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        curr = ''
        n = len(nums)
        ans = []
        def solve(curr,nums,n,ans):         #do->explore->undo
            if curr not in nums and len(curr)==n:
                ans.append(curr)
                return 
            if len(curr) == n:
                return 
            for ch in ['0','1']:
                curr = curr + ch 
                solve(curr,nums,n,ans)
                curr = curr[:-1]
        solve(curr,nums,n,ans)
        return ans[0]
