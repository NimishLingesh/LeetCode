# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self) -> None:
        self.p_trace = []
        self.q_trace = []
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_queue = [root]
        while p_queue:
            node = p_queue.pop(0)
            self.p_trace.append(node)
            if node.left:
                p_queue.append(node.left)
            if node.right:
                p_queue.append(node.right)
            
        q_queue = [root]
        while q_queue:
            node = q_queue.pop(0)
            self.q_trace.append(node)
            if node.left:
                q_queue.append(node.left)
            if node.right:
                q_queue.append(node.right)

        p_queue.reverse()
        for node_ele in p_queue:
            if node_ele in q_queue:
                return node_ele
