# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        rev = None
        if head != None:
            rev = head
            head = head.next
            rev.next = None
        while head != None:
            head_1 = head.next
            head.next = rev
            rev = head
            head = head_1
        return rev



sol = Solution()
l1 = []

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

h = sol.reverseList(head)

while h != None:
    print(h.val)
    h = h.next