"""LeetCode

Algorithm : 
    Sorting
Level :
    Medium
Status :
    Accepted

Tue Nov 28 23:07:47 PST 2023
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums.sort()

        for i in range(len(nums)):
            j, k = i+1, len(nums)-1
            while j < k:
                sum = nums[i]+nums[j]+nums[k]
                if sum == 0:
                    if [nums[i], nums[j], nums[k]] not in result:
                        result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1

        return result
        
