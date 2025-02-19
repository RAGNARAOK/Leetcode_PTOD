# Intuition
# Backtracking is very simple .This is having 3 steps
# 1.Do->2.Explore->3.Undo and repeat this untill we meet the base case
#----------------------------------------------------------------------Time complexity: O(N*2^N)-------------------------------------------------------------------------------

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        curr = ''
        result = []
        def solve(curr,result,n):       #do
            if len(curr) == n:          # base case if the crrent expression lenght is n then we need to stop exploring 
                result.append(curr)
                return 
            
            for ch in range(ord('a'),ord('c')+1):   #exploring. the last character should not be same and the lenth should not be 0 
                ch = chr(ch)
                if(len(curr)!=0 and curr[-1]==ch):
                    continue
                curr = curr+ch
                solve(curr,result,n)
                curr = curr[:-1]    # undo
        
        solve(curr,result,n)
        if k > len(result) :
            return ""
        return result[k-1]
