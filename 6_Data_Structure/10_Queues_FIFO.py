# Queues or FIFO works like a restaurant queue, the first one to get in, is the first to get out
# or served. The below code shows just that
# An important thing to note is that when the element is removed from the start unlike LIFO, there is a big performance
# impact because all the other elements will have to shift position in memory
# To do this we use DeQueue

from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)

queue.popleft()
print(queue)

if not queue:
    print("Disable")
