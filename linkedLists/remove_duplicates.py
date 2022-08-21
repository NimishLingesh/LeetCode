# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # a = -201
        # top = ListNode(-999)
        # prev = top
        # prev.next = head
        # first = prev.next
        # # second = first.next
        # # top.next = head
        # while first.next != None:
        #     if first.val == a:
        #         while first.val != first.next.val and first != None:
        #             first = first.next
        #         prev.next = first
        #     else:
        #         a = first.val
        list_a = set()
        list_b = set()
        cur = head
        while cur != None:
            num = cur.val
            if num not in list_a:
                list_a.add(num)
            else:
                list_b.add(num)
            cur = cur.next

        # print(list_b)
        prev = ListNode(-999)
        final = prev
        first = head
        prev.next = first
        while first != None:
            # import pdb

            # pdb.set_trace()
            if first.val in list_b:
                first = first.next
            else:
                tmp = first.next
                prev.next = first
                prev = first
                first = tmp
        prev.next = first
        return final.next


sol = Solution()
l = [1, 1]
cur = None
for i in l:
    node = ListNode(i)
    if cur == None:
        cur = node
        head = cur
        continue
    cur.next = node
    cur = cur.next
h = sol.deleteDuplicates(head)
while h != None:
    print(h.val)
    h = h.next
