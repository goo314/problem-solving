class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        # [4,2,7,6,9,14,12]
        # -2 5 -1 3 5 -2
        # bricks=5, ladders=1
        
        # 3 5
        # 3 5 5


        import heapq

        pq = []
        tmp = 0
        for i in range(len(heights) - 1):
            diff = heights[i+1] - heights[i]

            if diff > 0:
                heapq.heappush( pq, diff )
            
            if len(pq) > ladders:
                tmp += heapq.heappop(pq)
                if tmp > bricks:
                    return i
                    
        return len(heights)-1

        """
        i = 1
        while i < n:
            while ladders:


        # heapq
        import heapq
        pq = []
        heapq.heappush(pq, x)
        x = heapq.heappop(pq)

        n = len(heights)

        l = ladders
        
        i = 1
        while i < n:
            diff = heights[i] - heights[i-1]
            i += 1
            if diff < 0:
                continue

            heapq.heappush(pq, diff)    
            l -= 1
            if l == 0:
                break  
        
        while i < n:
            diff = heights[i] - heights[i-1]
            i += 1
            if diff < 0:
                continue
            heapq.heappush(pq, diff)
            
            tmp = 0
            while len(pq) > ladders:
                tmp += heapq.heappop(pq)
                # push again????
            if tmp < bricks:
                break
        return i

        """

