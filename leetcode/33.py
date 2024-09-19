"""LeetCode

Algorithm : 
    Binary Search
Level :
    Medium
Status :
    Accepted

Sun Dec  3 18:50:07 PST 2023
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1

        n = len(nums)
        start, end = 0, n-1
        while start <= end:
            mid = (start+end) // 2
            if nums[mid] == target:
                result = mid
                break
            
            # A B C
            if nums[start] < nums[mid] < nums[end]:
                if target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            # C A B
            elif nums[mid] < nums[end] < nums[start]:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            # B C A
            else:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

        return result