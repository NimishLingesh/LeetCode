class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ################### code from discussion - right approach
        if root == None:
            return 
        queue = []
        results = []
        queue.append(root)
        while queue:
            level = []
            for i in range(len(queue)):
                current_node = queue.pop(0)
                level.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            results.append(level)
        return results



        ############################### My code
        if root is None:
            return []
        traverse = [root]
        res = []
        while len(traverse)>0:
            tmp_lst = []
            for i in range(len(traverse)):
                tree = traverse.pop(0)
                tmp_lst.append(tree.val)
                if tree.left:
                    traverse.append(tree.left)
                if tree.right:
                    traverse.append(tree.right)
            res.append(tmp_lst)
        return res  


sol = Solution()
sol.levelOrder()