# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # if k > len()
        self.tree_l = []
        def traverse(root):
            if root == None:
                return
            traverse(root.left)
            self.tree_l.append(root.val)
            traverse(root.right)
            
            return
        traverse(root)
        return self.tree_l[k-1]