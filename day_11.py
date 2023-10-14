import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class merger:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two_lists(l1, l2):
            dummy = ListNode()
            current = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            current.next = l1 or l2
            return dummy.next

        min_heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i))

        dummy = ListNode()
        current = dummy

        while min_heap:
            val, i = heapq.heappop(min_heap)
            current.next = ListNode(val)
            current = current.next

            if lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(min_heap, (lists[i].val, i))

        return dummy.next


if __name__ == "__main__":
    # Example 1
    lists1 = [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]
    merger = merger()
    result1 = merger.mergeKLists(lists1)
    while result1:
        print(result1.val, end=" -> ")
        result1 = result1.next
    # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

