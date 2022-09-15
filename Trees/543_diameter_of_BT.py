# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.max_len = 0
        self.helper(root)
        return self.max_len

    def helper(self, root):
        if root == None:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        length = left + right
        self.max_len = max(self.max_len, length)
        return max(left, right) + 1

    # Good start, fails in the test case where the lenght is sound max on one side of the tree
    '''
    def __init__(self) -> None:
        self.left = 1
        self.right = 1
        self.tree_len = 0
        
    def diameterOfBinaryTree(self, root) -> int:
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        self.helper(root.left, "left")
        self.tree_len = 0
        self.helper(root.right, "right")
        return self.left + self.right


    def helper(self, root, left_or_right):
        if root == None:
            return
        if root.left == None and root.right == None:
            self.tree_len += 1
            if left_or_right == "left":
                if self.tree_len > self.left:
                    self.left = self.tree_len
            else:
                if self.tree_len > self.right:
                    self.right = self.tree_len
            self.tree_len -= 1
            return
        self.helper(root.left)
        self.helper(root.right)
        self.tree_len -= 1
    '''