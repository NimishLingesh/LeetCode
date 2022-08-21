# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x=0):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # prev = head
        # prev_idx = 0
        # first = head
        # if first == None:
        #     return None
        # if first.next == first:
        #     return first
        # second = head.next

        # while(first != None and second != None):
        #     # import pdb
        #     # pdb.set_trace()
        #     prev = first
        #     prev_idx += 1
        #     first = first.next
        #     if second.next == None:
        #         return None
        #     second = second.next.next
        #     if first == second:
        #         if second.next == first:
        #             return first
        #         return prev
        # return None

        prev = head
        prev_idx = 0
        first = head
        if first == None:
            return None
        # if first.next == first:
        #     return first
        # second = head.next
        nodes = []
        while(first != None):
            prev = first
            prev_idx += 1
            if first in nodes:
                return prev
            nodes.append(first)
            first = first.next
        return None

        
sol = Solution()
l1 = [1]
pos = -1
head = ListNode()

cur = None
pos_node = None
for idx, i in enumerate(l1):
    node = ListNode(i)
    if idx == pos:
        pos_node = node
    if cur == None:
        cur = node
        head = cur
        continue
    cur.next = node
    cur = cur.next
if pos_node:
    cur.next = pos_node

h = sol.detectCycle(head)
print(h.val)