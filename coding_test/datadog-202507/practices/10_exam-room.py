"""Practices

Algorithm :
    Balanced Binary Tree
Level :
    Medium
"""
import heapq
class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.left = {-1: (-1, n)}
        self.right = {n: (-1, n)}
        self.pq = [(n, -1, n)]
    
    def dist(self, x, y):
        if x == -1:
            return -y
        elif y == self.n:
            return -(self.n-1-x)
        else:
            return -((y-x)//2)
    
    def add(self, x, y):
        heapq.heappush(self.pq, (self.dist(x, y), x, y))
        self.left[x] = (x, y)
        self.right[y] = (x, y)
    
    def remove(self, x, y):
        self.pq.remove((self.dist(x, y), x, y))
        heapq.heapify(self.pq)
        del self.left[x]
        del self.right[y]

    def seat(self) -> int:
        _, x, y = heapq.heappop(self.pq)

        if x == -1:
            s = 0
        elif y == self.n:
            s = self.n-1
        else:
            s = (x+y)//2
        
        self.add(x, s)
        self.add(s, y)
        return s

    def leave(self, p: int) -> None:
        l, _ = self.right[p]
        _, r = self.left[p]

        self.remove(l, p)
        self.remove(p, r)
        self.add(l, r)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
