# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if not head or left == right:
            return head
        
        dummy = ListNode(0, head)
        prev = dummy
        
        # 1. Reach the node right before the `left` position
        for _ in range(left - 1):
            prev = prev.next
            
        # 2. `curr` stays at the original start of the reversed block
        curr = prev.next
        
        # 3. Perform sublist reversal in-place
        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
            
        return dummy.next
