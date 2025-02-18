# Time Complexity : O(N)
# Space Complexity : O(N)

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        stack = []
        counter = 1
        nums = ""

        for i in range(n+1):
            stack.append(str(counter))
            counter +=1

            if (i==n or pattern[i] == 'I'):
                while(len(stack)):
                    temp = stack[-1]
                    stack.pop()
                    nums += temp
        return nums

