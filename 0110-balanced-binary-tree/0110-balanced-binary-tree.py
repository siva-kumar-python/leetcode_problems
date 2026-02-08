# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans=True
        def height(temp):
            if temp is None:
                return 0

            left = height(temp.left)
            right = height(temp.right)

            if abs(left-right)>1:
                self.ans=False 
            return 1+max(left,right)
        height(root)
        return self.ans