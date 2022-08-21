# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self) -> None:
        self.res = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return
        self.inorderTraversal(root.left)
        self.res.append(root.val)
        self.inorderTraversal(root.right)


# sol = Solution()
# lst = [1, null, 2, 3]
# for ele, idx in enumerate(lst):
#     node = TreeNode(ele)

# sol.inorderTraversal(root)
