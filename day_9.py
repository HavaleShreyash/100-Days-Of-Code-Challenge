from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)  
        current = dummy_head  
        carry = 0  

        while l1 or l2:
            # Get the values of the current nodes in l1 and l2 (or 0 if l1 or l2 is None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum of values from l1, l2, and carry
            total_sum = val1 + val2 + carry
            carry = total_sum // 10 

            # Create a new node with the value of the current sum
            current.next = ListNode(total_sum % 10)
            current = current.next  

            # Move to the next nodes in l1 and l2 (if they exist)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # If there's still a carry after processing all digits, create a new node for it
        if carry > 0:
            current.next = ListNode(carry)

        return dummy_head.next  

# Helper function to convert a list of digits to a linked list
def list_to_linked_list(digits):
    dummy_head = ListNode()
    current = dummy_head
    for digit in digits:
        current.next = ListNode(digit)
        current = current.next
    return dummy_head.next

# Helper function to convert a linked list to a list of digits
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

if __name__ == "__main__":
    #sample
    l1 = list_to_linked_list([3, 4, 2])
    l2 = list_to_linked_list([5, 6, 4])

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    result_list = linked_list_to_list(result)

    print(result_list) 
