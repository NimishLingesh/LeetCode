# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.visited_nodes = []
        self.count = 0
        
    def pseudoPalindromicPaths (self, root) -> int:
        self.num_pseudo_palindromic = 0
        def is_pseudo_palindromic(path: dict) -> bool:
            one_odd = False
            for count in path.values():
                if count % 2 == 1:
                    if one_odd:
                        return False
                    one_odd = True
            return True
            
        def helper(node: Optional[TreeNode], path: dict):
            if node:
                path[node.val] += 1
                if not node.left and not node.right:
                    if is_pseudo_palindromic(path):
                        self.num_pseudo_palindromic += 1
                helper(node.left, path)
                helper(node.right, path)
                path[node.val] -= 1
        helper(root, defaultdict(int))
        return self.num_pseudo_palindromic



    # # ANOTHER SIMILAR APPROACH
    '''
    def __init__(self) -> None:
        self.visited_nodes = []
        self.count = 0
        
    def pseudoPalindromicPaths (self, root) -> int:
        if root == None:
            self.check_palindrome()
            self.visited_nodes.pop(-1)
        self.visited_nodes.append(root.val)
        self.pseudoPalindromicPaths(root.left)
        self.pseudoPalindromicPaths(root.right)
        return self.count

    def check_palindrome(self):
        # this works, but not optimal
        # ch_dict = {}
        # count = 0
        # for ch in self.visited_nodes():
        #     if ch not in ch_dict:
        #         ch_dict[ch] = 1
        #     else: 
        #         ch_dict[ch] += 1
        # visited = 0
        # valid_palindrome = 1
        # for key, value in ch_dict.items():
        #     if value%2 == 1 and not visited:
        #         visited = 1
        #         count += value
        #     elif value%2 == 1:
        #         count += value - 1
        #         valid_palindrome = 0
        #         break
        #     else:
        #         # for all even occurances
        #         count += value
        # if valid_palindrome:
        #     if count > self.count:
        #         self.count = count

        #  OPTIMAL SOLUTION
        is_palindrom = 0

        for i in range(1, 10):
            if self.visited_nodes.count(i) % 2 == 1:
                is_palindrom += 1
                if is_palindrom > 1:
                    return False

        self.count += 1
    '''