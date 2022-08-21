class Solution(object):
    def __init__(self):
        self.results = []
        
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.traverse(root)
        return self.results
            
    def traverse(self, var):
        if var == None:
            return
        print(var.val)
        self.results.append(var.val)
        if var.children:
            for ch in var.children:
                self.traverse(ch)