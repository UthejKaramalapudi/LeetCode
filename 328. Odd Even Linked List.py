# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        n = head
        m = head.next
        m_head = m

        while m and m.next:
            n.next = m.next
            n = n.next
            m.next = m.next.next
            m = m.next

        n.next = m_head
        return head
