# https://leetcode.com/problems/contains-duplicate/

def containsDuplicate1(nums) -> bool:
    for n in nums:
        count = 0
        for m in nums:
            if n == m:
                count += 1
            if count == 2:
                return True
        
    return False



def containsDuplicate2(nums) -> bool:
    nums.sort()

    for i in range(len(nums) - 2):
        if nums[i] == nums [i+1]:
            return True
        
    return False


def containsDuplicate3(nums) -> bool:
    nums_set = set(nums)

    if len(nums_set) != nums:
        return True
        
    return False


def containsDuplicate4(nums) -> bool:
    nums_set = set(nums)
    if len(nums_set) != len(nums):
        return True
        
    return False


def containsDuplicate(nums) -> bool:
    nums_set = set()
    for n in nums:
        if n in nums_set:
            return True
        else:
            nums_set.add(n)
    return False



nums = [1, 2, 3, 1]
print(containsDuplicate(nums=nums))
