class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        
        current = dummy
        
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next
    
head = ListNode(
    1, ListNode(2, ListNode(6, ListNode(3, ListNode(6))))
)

s = Solution()
result = s.removeElements(head, 6)
while result:
    print(result.val, end=" ")
    result = result.next
