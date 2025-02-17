#-------------------------------------------------------------------Brute Force Approach -----------------------------------------------------------------------------------------
#-----------------------------------------------------------------Time complexity : O(n*w)where w is fixed here ---------------------------------------------------------------------

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        w = len(part)
        i = 0 
        while i< len(s):
            if s[i]==part[0] and s[i:w] == part:
                i+=w
            else:
                stack.append(s[i])
        return ''.join(stack)

#--------------------------------------------------------------------- Approach 2 -----------------------------------------------------------------------------------------------
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
    
        stack = []
        part_length = len(part)
        for char in s:
            stack.append(char)
            if len(stack) >= part_length:
                if ''.join(stack[-part_length:]) == part :
                    for i in range(part_length):
                        stack.pop()

        return ''.join(stack)
