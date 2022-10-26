# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        traverse = [root]
        res = []
        left_to_right = False
        while len(traverse)>0:
            tmp_lst = []
            for i in range(len(traverse)):
                tree = traverse.pop(0)
                if left_to_right:
                    # insert to the front of the list
                    tmp_lst.insert(0, tree.val)
                else:
                    # insert the node to the end of the list
                    tmp_lst.append(tree.val)
                if tree.left:
                    traverse.append(tree.left)
                if tree.right:
                    traverse.append(tree.right)
            if left_to_right:
                left_to_right = False
            else:
                left_to_right = True
            res.append(tmp_lst)
        return res        
        
        