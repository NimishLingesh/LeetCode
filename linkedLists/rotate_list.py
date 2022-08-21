# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head

        cpy = head
        count = 1
        while cpy.next != None:
            count += 1
            cpy = cpy.next
        rng = int(k % count)
        # print("range - ", rng)
        # another approach is to split the ll and join in the beginning
        for i in range(0, rng):
            head = self.rotateOnce(head)
        return head

    def rotateOnce(self, head):
        prev = head
        cur = head.next
        while cur.next is not None:
            prev = cur
            cur = cur.next
        prev.next = None
        cur.next = head
        return cur


sol = Solution()
l = [1, 2, 3]
cur = None
for i in l:
    node = ListNode(i)
    if cur == None:
        cur = node
        head = cur
        continue
    cur.next = node
    cur = cur.next
h = sol.rotateRight(head, 4)
while h != None:
    print(h.val)
    h = h.next
