# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        cur = head
        while cur != None:
            count += 1
            cur = cur.next

        num = count - n
        if num == 0:
            return head.next
        prev = head
        cur = head.next

        num -= 1

        while cur != None:
            if num == 0:
                tmp = cur
                cur = tmp.next
                prev.next = cur
                if cur == None:
                    break
                del tmp
            num -= 1
            prev = cur
            cur = cur.next

        return head


sol = Solution()
l = [1, 2, 3, 4, 5]
cur = None
for i in l:
    node = ListNode(i)
    if cur == None:
        cur = node
        head = cur
        continue
    cur.next = node
    cur = cur.next
h = sol.removeNthFromEnd(head, 5)

while h != None:
    print(h.val)
    h = h.next
