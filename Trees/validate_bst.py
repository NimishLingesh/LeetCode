# Definition for a binary tree node.
from selectors import EpollSelector
import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.bst = True 
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.checkValidity(root, -sys.maxsize, sys.maxsize)
        return self.bst
        

    def checkValidity(self, root, min, max):
        if root == None:
            return
        print(root.val, min, max)
        if root.val>min and root.val<max:
            self.checkValidity(root.left, min, root.val)
            self.checkValidity(root.right, root.val, max)
        else:
            self.bst = False
        
        
sol = Solution()
tree = [2,1,3]
for ele, idx in enumerate(tree):
    node = TreeNode(ele)

sol.isValidBST(root)

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         if self.checkValidity(root) is None:
#             return True
#         else:
#             return False
        

#     def checkValidity(self, root):
#         if root == None:
#             return
#         if root.left:
#             if self.compareLowHigh(root.left.val, root.val):
#                 self.checkValidity(root.left)
#             else:
#                 return False
#         if root.right:
#             if self.compareLowHigh(root.val, root.right.val):
#                 self.checkValidity(root.right)
#             else:
#                 return False

#     def compareLowHigh(self, low, high):
#         if low<high:
#             return True
#         else:
#             return False
        