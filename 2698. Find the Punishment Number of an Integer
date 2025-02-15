class Solution:
    def canPartition(self, num: str, target: int, index: int, current_sum: int) -> bool:
        """ Recursively checks if num can be split to sum to target """
        if index == len(num):
            return current_sum == target  # Base case: check if sum matches target
        
        for j in range(index, len(num)):  # Try splitting at different positions
            part = int(num[index:j+1])  # Convert substring to number
            if current_sum + part > target:
                break  # Stop early if sum exceeds target
            if self.canPartition(num, target, j+1, current_sum + part):
                return True  # Found a valid partition

        return False

    def punishmentNumber(self, n: int) -> int:
        total = 0
        for i in range(1, n + 1):
            square_str = str(i * i)
            if self.canPartition(square_str, i, 0, 0):  # Check if i can be formed
                total += i * i
        return total
