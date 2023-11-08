from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = head.next
        head.next = head.next.next
        new_head.next = head

        current = head.next
        prev = head

        while current and current.next:
            temp = current.next
            current.next = current.next.next
            temp.next = current

            prev.next = temp
            prev = current
            current = current.next

        return new_head

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    solution = Solution()
    print(solution)
