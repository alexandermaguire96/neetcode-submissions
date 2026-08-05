# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        
        slow, fast = head, head
        s, f = slow, fast

        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False