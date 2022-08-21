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



        ############################### My code, not completely correct
        queue = []
        if root == None:
            return []
        queue.append(root)
        level = 0
        res_dict = {}
        res_dict["0"] = root.val
        level = 0
        while queue:
            # lst = []
            # print(queue)
            node = queue.pop(0)
            temp = 0
            # lst.append(node.val)
            if node.left:
                temp = 1
                level += 1
                queue.append(node.left)
                if res_dict.get(level):
                    res_dict[level].append(node.left.val)
            if node.right:
                if not temp:
                    level += 1
                queue.append(node.right)
                if res_dict.get(level):
                    res_dict[level].append(node.right.val)
        return res_dict.values()
        # # sorted_dict = {k: v for k, v in sorted(res_dict.items(), key=lambda item: item[1])}
        # final_dict = {}
        # # final_dict = [sorted_dict.get("0")]
        # for val, level in res_dict.items():
        #     if level not in final_dict.keys():
        #         final_dict[level] = [val]
        #     else:
        #         final_dict[level].append(val)

        # print(final_dict)
        # return final_dict.values()


sol = Solution()
sol.levelOrder()