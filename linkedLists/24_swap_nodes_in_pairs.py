# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        first = head
        if head == None or head.next == None:
            return head
        if first.next:
            tmp = first.next.next
            head = first.next
            head.next = first
            first = head.next
            first.next = tmp
        prev = first
        first = first.next
        # print(first.next)
        while first != None and first.next!= None:
            # next_set = first.next.next
            # tmp = first.next
            # prev.next = tmp
            # tmp.next = first
            # first.next = next_set
            # first = first.next
            second = first.next
            next_set = second.next

            # first.next = next_set
            prev.next = second
            second.next = first
            first.next = next_set
            prev = first
            first = first.next
        return head


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
h = sol.swapPairs(head)
while h != None:
    print(h.val)
    h = h.next