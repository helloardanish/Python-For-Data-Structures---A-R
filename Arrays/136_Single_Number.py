# https://leetcode.com/problems/single-number/description/

from typing import List


class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
            if count == 1:
                return nums[i]

class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums) -1, 2):
            if nums[i-1] != nums[i]:
                return nums[i-1]
        
        return nums[len(nums) - 1]


class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        dict_num = {}
        for i in range(len(nums)):
            if nums[i] in dict_num:
                dict_num[nums[i]] = dict_num[nums[i]] + 1
            else:
                dict_num[nums[i]] = 1

        for key, val in dict_num.items():
            if val == 1:
                return key
        

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            ans = ans ^ n
        return ans


s = Solution()
nums = [2,3,5,2,5]
print(s.singleNumber(nums))

