# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        seen = set()
        seen.add(head)
        while head.next:
            head = head.next
            if head in seen:
                return True
            seen.add(head)
        return False