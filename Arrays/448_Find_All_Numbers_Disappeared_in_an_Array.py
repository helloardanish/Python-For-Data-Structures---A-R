# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

from typing import List


class Solution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            j = i + 1
            found = False
            for val in nums:
                if j == val:
                    found = True
            if not found:
                ans.append(j)
        return ans
    
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            val = 0
            if nums[i] > 0:
                val = nums[i]
            else:
                val = nums[i] * -1

            if nums[val - 1] > 0:
                nums[val - 1] = nums[val - 1] * -1
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        return ans

            

s = Solution()
inputarr = [1,2,2,2]
print(s.findDisappearedNumbers(inputarr))
