# Stack (LIFO - Last In First Out)
stack = []
stack.append(1)  # Push
stack.append(2)
stack.append(3)
print("Stack after pushes:", stack)
popped = stack.pop()  # Pop
print("Popped from stack:", popped)
print("Stack after pop:", stack)

# Queue (FIFO - First In First Out)
from collections import deque
queue = deque()
queue.append(1)  # Enqueue
queue.append(2)
queue.append(3)
print("\nQueue after enqueues:", list(queue))
dequeued = queue.popleft()  # Dequeue
print("Dequeued from queue:", dequeued)
print("Queue after dequeue:", list(queue))
