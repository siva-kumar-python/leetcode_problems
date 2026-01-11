# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 1
        ans=[]
        q = deque()
        q.appendleft(root)
        ans.append(root.val)
        maxel=0
        maxlvl=1
        count=1
        while len(q):
            res=[]
            for i in range(len(q)):
                temp = q.pop()
                if temp.left:
                    q.appendleft(temp.left)
                    res.append(temp.left.val)
                if temp.right:
                    q.appendleft(temp.right)
                    res.append(temp.right.val)
            if len(res):
                ans.append(sum(res))
        
        return ans.index(max(ans))+1

