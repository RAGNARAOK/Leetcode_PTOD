class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        # Array to count incoming edges (favorites)
        indegree = [0] * n
        # Queue for processing nodes
        queue = [0] * n
        # Depth array to track the longest chain leading to each employee
        depth = [0] * n
        
        # Count the number of favorites for each employee
        for i in range(n):
            indegree[favorite[i]] += 1

        # Left pointer for the queue
        left = 0
        # Right pointer for the queue
        right = 0
        
        # Initialize the queue with employees who have no favorites (indegree == 0)
        for i in range(n):
            if indegree[i] == 0:
                queue[right] = i
                right += 1

        # Process the queue
        while left < right:
            # Current employee being processed
            current = queue[left]
            left += 1
            # The favorite of the current employee
            next_employee = favorite[current]
            
            # Update the depth for the next employee
            depth[next_employee] = max(depth[next_employee], depth[current] + 1)
            
            # Decrease the indegree of the next employee
            indegree[next_employee] -= 1
            
            # If the next employee has no more incoming edges, add them to the queue
            if indegree[next_employee] == 0:
                queue[right] = next_employee
                right += 1

        # To count the total from small circles (size 2)
        small_circle = 0
        # To track the largest circle size
        big_circle = 0

        # Check for remaining employees that are part of cycles
        for i in range(n):
            # If this employee is part of a cycle
            if indegree[i] != 0:
                # Mark as processed
                indegree[i] = 0
                # Start counting the size of the cycle
                count = 1
                j = favorite[i]  # Start from the favorite of the current employee
                
                # Traverse the cycle
                # Continue until we return to the starting employee
                while j != i:
                    count += 1
                    # Mark as processed
                    indegree[j] = 0
                    # Move to the next favorite
                    j = favorite[j]

                # If the cycle size is 2, calculate the contribution to small circles
                if count == 2:
                    small_circle += depth[i] + depth[favorite[i]] + 2
                else:
                    # Update the largest circle size found
                    big_circle = max(big_circle, count)

        # Return the maximum of the largest circle size or the total from small circles
        return max(big_circle, small_circle)
        
