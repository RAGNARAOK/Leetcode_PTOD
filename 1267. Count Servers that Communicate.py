class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        n = len(grid[0])
        m= len(grid)
        len_row = [0]*m
        len_col = [0]*n
        for row in range(m):        #preprocess the information of servers in a row and col
            for col in range(n):
                if grid[row][col] == 1:
                    len_row[row]+=1
                    len_col[col]+=1

        ans = 0
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    if len_row[row] >=2 or len_col[col]>=2:
                        ans+=1

        return ans
