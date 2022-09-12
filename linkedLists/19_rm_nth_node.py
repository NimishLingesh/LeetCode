# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total_node = 0
        main_head = head
        while head.next != None:
            head = head.next
            total_node += 1
        idx = total_node - n + 1
        head = main_head
        i = 0
        prev = None
        
        
        while i < idx:
            i += 1
            prev = head
            head = head.next
            
        if idx == 0:
            return head.next
        elif prev:
            tmp = head
            prev.next = head.next
            del tmp
        return main_head
        