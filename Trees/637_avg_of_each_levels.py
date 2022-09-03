# Definition for a binary tree node.
from re import L


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root):
        res = [root.val]
        q_nodes = [root]
        while len(q_nodes) != 0:
            sum_node = 0
            cnt = 0
            for i in range(len(q_nodes)):
                node = q_nodes.pop(0)
                cnt += 1
                sum_node += node.val
                if node.left:
                    q_nodes.append(node.left)
                if node.right:
                    q_nodes.append(node.right)
            if cnt != 0:
                res.append(sum_node/cnt)
        return res[1:]

sol = Solution()
sol.averageOfLevels()