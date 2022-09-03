# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def __init__(self) -> None:
#         self.p_trace = []
#         self.q_trace = []
        
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """
#         p_queue = [root]
#         while p_queue:
#             node = p_queue.pop(0)
#             self.p_trace.append(node)
#             if node.left:
#                 p_queue.append(node.left)
#             if node.right:
#                 p_queue.append(node.right)
            
#         q_queue = [root]
#         while q_queue:
#             node = q_queue.pop(0)
#             self.q_trace.append(node)
#             if node.left:
#                 q_queue.append(node.left)
#             if node.right:
#                 q_queue.append(node.right)

#         p_queue.reverse()
#         for node_ele in p_queue:
#             if node_ele in q_queue:
#                 return node_ele


# BOTTOM UP APPROACH    
class Solution(object):
    def __init__(self):
        self.p_trace = []
        self.q_trace = []

    def lowestCommonAncestor(self, root, p, q):
        self.trace_nodes(root, p, "p")
        self.trace_nodes(root, q, "q")
        if len(self.p_trace) < len(self.q_trace):
            for q in self.q_trace:
                if q in self.p_trace:
                    return q
        else:
            for p in self.p_trace:
                if p in self.q_trace:
                    return p

    def trace_nodes(self, tree, node_val, p_or_q):
        if tree == None:
            return 
        if tree == node_val:
            if p_or_q == "p":
                self.p_trace.append(tree)
            else:
                self.q_trace.append(tree)
            return True
        set_tmp = False
        left_traversal = self.trace_nodes(tree.left, node_val, p_or_q)
        if left_traversal == True:
            if p_or_q == "p":
                self.p_trace.append(tree)
            else:
                self.q_trace.append(tree)
            set_tmp = True
        right_traversal = self.trace_nodes(tree.right, node_val, p_or_q)
        if right_traversal == True:
            if p_or_q == "p":
                self.p_trace.append(tree)
            else:
                self.q_trace.append(tree)
            set_tmp = True
        if set_tmp:
            return True

sol = Solution()
sol.lowestCommonAncestor(p, q)