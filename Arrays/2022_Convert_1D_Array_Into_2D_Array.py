# https://leetcode.com/problems/convert-1d-array-into-2d-array/description/

from typing import List


class Solution1:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        ans = []
        for i in range(0,m*n,n):
            sub_arr_1d = []
            index = i
            for j in range(n):
                sub_arr_1d.append(original[index])
                index += 1
            ans.append(sub_arr_1d)
        return ans
    
class Solution2:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        ans = []
        # 0>0,1,2, 1>3,4,5 : m = 3, n=2
        # 0>0, 1, 1>2, 3, 2> 4, 5 : m=2, n=3
        for i in range(m):
            start = n*i
            end = n*i + n
            sub_arr_1d = []
            for j in range(start, end):
                sub_arr_1d.append(original[j])

            ans.append(sub_arr_1d)
        
        return ans
    
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        ans = []
        for i in range(m):
            sub_arr_1d = original[(n*i): (n*i + n)]
            ans.append(sub_arr_1d)
        return ans

inp = [1,3,2,4,6,5]
# inp = [3]
s = Solution1()
print(s.construct2DArray(inp, 3, 2))
            
        