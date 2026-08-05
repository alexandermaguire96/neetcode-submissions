# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def rec(curr, distance, n, new_next):
    
            # base case
            if not curr:
                return distance, new_next

            # recursive call
            distance, new_next = rec(curr.next, distance, n, new_next)
            distance += 1
            if distance == n-1:
                new_next = curr
            elif distance == n + 1:
                curr.next = new_next

            return distance, new_next


        distance, new_next = rec(head, 0, n, None)
        if distance == n:
            return head.next
        return head