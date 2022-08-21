# Definition for singly-linked list.
from operator import truediv


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first = head
        if head.next != None:
            second = head.next
        else:
            return first
        tmp = True
        while tmp:
            if second.next == None:
                return first.next
            if second.next.next == None:
                return first.next
            first = first.next
            second = second.next.next

sol = Solution()
l1 = [1,2,3,4,5,6]

head = ListNode()

cur = None
for i in l1:
    node = ListNode(i)
    if cur == None:
        cur = node
        head = cur
        continue
    cur.next = node
    cur = cur.next

h = sol.middleNode(head)

while h != None:
    print(h.val)
    h = h.next