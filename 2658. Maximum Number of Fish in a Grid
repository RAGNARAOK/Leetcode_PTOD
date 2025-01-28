from collections import deque

class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def bfs(self, i, j, grid):
        que = deque([(i, j)])
        fish_count = grid[i][j]
        grid[i][j] = 0  # Mark the cell as visited by setting it to 0

        while que:
            x, y = que.popleft()
            
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < self.m and 0 <= ny < self.n and grid[nx][ny] > 0:
                    que.append((nx, ny))
                    fish_count += grid[nx][ny]
                    grid[nx][ny] = 0  # Mark as visited

        return fish_count

    def findMaxFish(self, grid):
        self.m = len(grid)
        self.n = len(grid[0])

        max_fish = 0

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] > 0:  # Water cell found
                    max_fish = max(max_fish, self.bfs(i, j, grid))

        return max_fish
