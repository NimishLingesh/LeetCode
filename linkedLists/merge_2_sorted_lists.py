# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        final = head
        cur1 = list1
        cur2 = list2
        while cur1 != None or cur2 != None:
            if cur1 == None:
                head.next = cur2
                break
            elif cur2 == None:
                head.next = cur1
                break

            if cur1.val < cur2.val:
                head.next = cur1
                head = head.next
                cur1 = cur1.next
                if cur1 == None:
                    head.next = cur2
                    break
            else:
                head.next = cur2
                head = head.next
                cur2 = cur2.next
                if cur2 == None:
                    head.next = cur1
                    break
        return final.next


sol = Solution()
# l1 = [1, 2, 3, 4, 5]
# l2 = [4, 6, 7]
l1 = []
l2 = [0]
head1 = ListNode()
head2 = ListNode()

cur = None
for i in l1:
    node = ListNode(i)
    if cur == None:
        cur = node
        head1 = cur
        continue
    cur.next = node
    cur = cur.next

cur = None
for i in l2:
    node = ListNode(i)
    if cur == None:
        cur = node
        head2 = cur
        continue
    cur.next = node
    cur = cur.next

h = sol.mergeTwoLists(head1, head2)

while h != None:
    print(h.val)
    h = h.next
