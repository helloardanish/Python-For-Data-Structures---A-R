# https://leetcode.com/problems/missing-number/

from typing import List

class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [-1] * (len(nums)+1)
        
        print(arr)
        for i in range(len(nums)):
            arr[nums[i]] = nums[i]

        for i in range(len(arr)):
            if arr[i] == -1:
                return i

class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)):
            if i != nums[i]:
                print(i)
                return i

        return len(nums)
    

class Solution3:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actual_sum = (n*(n+1))//2
        current_sum = 0
        for n in nums:
            current_sum += n

        return actual_sum - current_sum

            


s = Solution3()
nums = [3, 0, 1, 2]
print(s.missingNumber(nums))
