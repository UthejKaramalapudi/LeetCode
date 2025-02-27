# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for i in range(left-1):
            prev = prev.next

        curr_node = prev.next
        prev1 = None

        for _ in range(right - left + 1):
            next_node = curr_node.next
            curr_node.next = prev1
            prev1 = curr_node
            curr_node = next_node

        prev.next.next = curr_node
        prev.next = prev1

        return dummy.next
