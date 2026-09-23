# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        # Step 1: Determine if a cycle exists using fast and slow pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # Fast and slow pointers meet inside the cycle
            if slow == fast:
                # Step 2: Find the start node of the cycle
                # Reset slow pointer to head and move both at speed 1
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow  # Both pointers now point to the start of the cycle
                
        return None  # No cycle found
