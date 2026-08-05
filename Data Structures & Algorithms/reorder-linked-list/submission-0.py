# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:

    
    def reorderList(self, head: Optional[ListNode]) -> None: 
        if not head or not head.next:
            return      
        # while head:
        #     rev_list.append(head.val)
        #     head = head.next
        # ^Reverse list of values, but we want a reverse list of nodes
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None

        #should have a list prev to slow.next, and curr to end.

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        #ends when we have prev the 2nd half fully reversed. And curr is empty

        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2



    
        


