# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        cnt = 1
        odd_ll = None
        even_ll = None

        main_even = None
        main_head = None
        while head != None:
            # if ODD
            tmp = head
            head = head.next
            tmp.next = None
            if cnt % 2 == 1:
                if odd_ll == None:
                    odd_ll = tmp
                    main_head = odd_ll
                else:
                    odd_ll.next = tmp
                    odd_ll = odd_ll.next
            else:
                if even_ll == None:
                    even_ll = tmp
                    main_even = even_ll
                else:
                    even_ll.next = tmp
                    even_ll = even_ll.next
            cnt += 1
        if main_even:
            odd_ll.next = main_even
        return main_head



sol = Solution()
l = [1,2,3,4,5]
cur = None
for i in l:
    node = ListNode(i)
    if cur == None:
        cur = node
        head = cur
        continue
    cur.next = node
    cur = cur.next
h = sol.oddEvenList(head)
while h != None:
    print(h.val)
    h = h.next