import sys

class CustomQueue:
    def init(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, element):
        self.enqueue_stack.append(element)

    def dequeue(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        if self.dequeue_stack:
            self.dequeue_stack.pop()

    def print_front(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        if self.dequeue_stack:
            print(self.dequeue_stack[-1])

def get_user_input():
   # print("Enter queries for the CustomQueue (1 x, 2, or 3) separated by commas:")
    return input().split(',')


queue = CustomQueue()
queries = get_user_input()
for query in queries:
    query_type, *args = map(int, query.split())
    if query_type == 1:
        queue.enqueue(args[0])
    elif query_type == 2:
        queue.dequeue()
    elif query_type == 3:
        queue.print_front()

#Sample Input:
#1 5, 1 10, 2, 1 3, 3
#Sample Output:
# 10
# 3
