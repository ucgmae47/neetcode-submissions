# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        node = ListNode(val = head.val)
        while head.next:
            head = head.next
            new_node = ListNode(val = head.val, next = node)
            node = new_node
        return node