"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newlist = None

        def helper(node, node_index):
            index_hashmap, random_hashmap, nodes = {}, {}, []
            temp = node
            while temp:
                index_hashmap[temp] = node_index
                index_hashmap[node_index] = temp
                temp = temp.next
                node_index += 1
            temp = node
            while temp:
                random_hashmap[temp] = index_hashmap[temp.random] if temp.random != None else None
                temp = temp.next
            dummy = Node(0)
            temp, newHead, i = node, dummy, 0

            
            print(index_hashmap)
            while temp:
                newHead.next = Node(temp.val)
                temp, newHead = temp.next, newHead.next
                index_hashmap[newHead] = i
                index_hashmap[i] = newHead
                i += 1
            print(index_hashmap)
            temp, tempOld = dummy.next, head
            while temp:
                temp.random = index_hashmap[random_hashmap[tempOld]] if random_hashmap[tempOld] is not None else None
                temp, tempOld = temp.next, tempOld.next

            return dummy.next
                
            
        newlist = helper(head, 0)
        return newlist