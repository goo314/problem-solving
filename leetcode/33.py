"""LongestPanlindrome

Algorithm : 
    Binary Search
Level :
    Medium
Status :
    Failed

Thu Nov 30 23:06:16 PST 2023
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1

        start, end = 0, len(nums)-1
        # Can't find pivot when start = end
        while start <= end:
            mid = (start+end)//2
            if not (nums[start] <= nums[mid]):
                end = mid - 1
            if not (nums[mid] <= nums[end]):
                start = mid + 1
            else:
                break
        
        start, end = start-len(nums), start-1
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                result = mid % len(nums)
                break
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return result
