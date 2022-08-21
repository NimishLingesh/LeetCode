# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        if l1 == None and l2 == None:
            return None
        elif l2 == None:
            return l1
        elif l1 == None:
            return l2

        l3 = ListNode()
        first = l3
        l3.val = (l1.val + l2.val) % 10
        carry = int((l1.val + l2.val) / 10)
        while l1.next != None and l2.next != None:
            l1 = l1.next
            l2 = l2.next

            temp = ListNode()
            temp.val = (l1.val + l2.val + carry) % 10
            # print(temp.val)
            carry = int((l1.val + l2.val + carry) / 10)
            l3.next = temp
            l3 = l3.next

        if l1.next != None:
            while l1.next != None:
                l1 = l1.next
                temp = ListNode()
                temp.val = (l1.val + carry) % 10
                carry = int((l1.val + carry) / 10)
                l3.next = temp
                l3 = l3.next

        elif l2.next != None:
            while l2.next != None:
                l2 = l2.next
                temp = ListNode()
                temp.val = (l2.val + carry) % 10
                carry = int((l2.val + carry) / 10)
                l3.next = temp
                l3 = l3.next

        if carry != 0:
            temp = ListNode()
            temp.val = carry
            l3.next = temp
            l3 = l3.next
        return first


sol = Solution()
l1 = ListNode(2)
l2 = ListNode(3)
cur = ListNode(4)
l2.next = cur
res = sol.addTwoNumbers(l1, l2)
print(res.val)
while res.next != None:
    res = res.next
    print(res.val)
