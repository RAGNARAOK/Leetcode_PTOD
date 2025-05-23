# -- problem Link : https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/description/?envType=daily-question&envId=2025-02-21
# -- Time complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        self._recover(root,0)

    def _recover(self,node,value):
        if not node:
            return
        node.val = value
        self.values.add(value)
            # recover the left and right nodes value recursively
        if node.left:
            self._recover(node.left,2*value+1)
        if node.right:
            self._recover(node.right,2*value+2)


    def find(self, target: int) -> bool:
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
