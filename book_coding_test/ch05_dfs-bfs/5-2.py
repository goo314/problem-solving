queue = []
queue.append(1)
queue.append(2)
queue.pop(0)

# more faster than list
from collections import deque
queue = deque()

queue.append(1)
queue.append(2)
queue.popleft()
queue.append(3)

print(queue)
