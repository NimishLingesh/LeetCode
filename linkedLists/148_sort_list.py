# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        self.final_tree = None
        self.final_head = None
        def construct_tree(node):
            if self.final_tree is None:
                self.final_tree = node
                self.final_head = self.final_tree
            self.final_tree.next = node
            self.final_tree = self.final_tree.next
            
        while head != None:
            min_val = head.val
            min_node = head
            min_prev = None
            
            prev = None
            tree = head
            while tree.next != None:
                prev = tree
                tree = tree.next
                if tree.val < min_val:
                    min_val = tree.val
                    min_node = tree
                    min_prev = prev
            min_prev = min_node.next
            min_node.next = None
            construct_tree(min_node)
            if min_node == head:
                head = head.next
                # break
            print(head)
            import time
            time.sleep(0.5)
        return self.final_head
            
    
        # 1. first node
        # 2. last node
        # 3. None
    
sol = Solution()
l = [1, 2, 3, 4, 5, 6]
cur = None
for i in l:
    node = ListNode(i)
    if cur == None:
        cur = node
        head = cur
        continue
    cur.next = node
    cur = cur.next
h = sol.sortList(head)