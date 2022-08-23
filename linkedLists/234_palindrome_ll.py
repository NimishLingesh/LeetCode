# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        second = head.next
        first = head
        first_half = []
        odd = True
        while second != None:
            first_half.append(first.val)
            first = first.next
            if second.next == None:
                odd = False
                break
            if second.next.next == None:
                odd = True
                break
            second = second.next.next
        
        if odd:
            first = first.next
        while first != None:
            ele = first_half.pop()
            if first.val != ele:
                return False
            first = first.next
        if len(first_half) != 0:
            return False
        else:
            return True

sol = Solution()
l = [1]
cur = None
for i in l:
    node = ListNode(i)
    if cur == None:
        cur = node
        head = cur
        continue
    cur.next = node
    cur = cur.next
h = sol.isPalindrome(head)
# while h != None:
#     print(h.val)
#     h = h.next
print(h)
