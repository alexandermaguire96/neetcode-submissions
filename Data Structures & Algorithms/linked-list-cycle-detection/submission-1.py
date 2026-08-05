# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        seen = set()
        check = head

        while check:
            if check in seen:
                return True

            seen.add(check)
            check = check.next

        return False
        