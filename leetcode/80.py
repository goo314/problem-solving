"""LeetCode

Algorithm : 
    Two Pointers
Level :
    Medium
Status :
    Accepted

Sat Sep 21 00:03:00 KST 2024
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        result = 0

        n = len(nums)
        arr = [0 for _ in range(n)]
        
        cnt = 1
        arr[0] = cnt
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                cnt += 1
            else:
                cnt = 1
            arr[i] = cnt
        
        for i in range(n):
            if arr[i] > 2:
                for j in range(i+1, n):
                    if arr[j] <= 2:
                        nums[i], nums[j] = nums[j], nums[i]
                        arr[i], arr[j] = arr[j], arr[i]
                        print(i, j)
                        break
        
        for x in arr:
            if x > 2:
                break
            result += 1
        
        return result

        """Better Answer
        n = len(nums)
        if n <= 2:
            return n
        
        j = 1
        for i in range(2, n):
            if nums[i] != nums[j-1]:
                j += 1
                nums[j] = nums[i]
        
        result = j+1
        return result
        """