# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def pruneTree(self, root):

        #  My solution doesnt work completely
        def bottomUp(tree):
            if tree == None:
                return None
            if tree.left == None and tree.right == None:
                return tree.val
            present = bottomUp(tree.left)
            # present = present or tree.val
            if present == 0 or present == None:
                tree.left = None
            present = bottomUp(tree.right)
            # present = present or tree.val
            if present == 0 or present == None:
                tree.right = None
            # bottomUp(root)
            return 1
        bottomUp(root)
        print(root)
        return root

    # def bottomUp(self, tree, one_present):
    #     if tree == None:
    #         return
    #     present = self.bottomUp(tree.left, one_present)
    #     present = present or tree.val
    #     if not present:
    #         tree.left = None
    #     present = self.bottomUp(tree.right, one_present)
    #     present = present or tree.val
    #     if not present:
    #         tree.right = None

    # correct solution
        if not root: return None
        root.left, root.right = self.pruneTree(root.left), self.pruneTree(root.right)
        return root if (root.left or root.right or root.val == 1) else None